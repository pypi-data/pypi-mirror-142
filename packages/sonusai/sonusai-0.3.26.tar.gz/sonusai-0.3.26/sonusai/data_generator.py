import multiprocessing
import random
import tempfile
from multiprocessing import Manager
from typing import List
from typing import Union

import h5py
import numpy as np
from pyaaware import FeatureGenerator
from tensorflow.keras.utils import Sequence

from sonusai import SonusAIError
from sonusai import logger
from sonusai.genft import genft
from sonusai.mixture import get_mixtures_from_mixid
from sonusai.utils import reshape_inputs


class DataGenerator(Sequence):
    """Generates data for Keras"""

    def __init__(self,
                 mixdb: dict,
                 mixid: Union[str, List[int]],
                 batch_size: int,
                 timesteps: int,
                 flatten: bool,
                 add1ch: bool,
                 shuffle: bool = False,
                 chunks: int = 16):
        """Initialization"""
        self.mixdb = mixdb
        self.mixid = mixid
        self.batch_size = batch_size
        self.timesteps = timesteps
        self.flatten = flatten
        self.add1ch = add1ch
        self.shuffle = shuffle
        self.chunks = chunks

        self.index_map = None
        self.total_batches = None
        self.frames_per_batch = None
        self.fetching = multiprocessing.Condition()

        self.cache_file = tempfile.TemporaryFile()
        manager = Manager()
        self.cache_line = manager.list()

        self.initialize_mixtures()

        fg = FeatureGenerator(frame_size=self.mixdb['frame_size'],
                              feature_mode=self.mixdb['feature'],
                              num_classes=self.mixdb['num_classes'],
                              truth_mutex=self.mixdb['truth_mutex'])
        feature, truth, _, _, _, _ = reshape_inputs(
            feature=np.single(np.random.random((self.batch_size, fg.stride, fg.num_bands))),
            truth=np.single(np.random.random((self.batch_size, fg.num_classes,))),
            batch_size=self.batch_size,
            timesteps=self.timesteps,
            flatten=self.flatten,
            add1ch=self.add1ch)

        with h5py.File(self.cache_file, 'a') as f:
            f.create_dataset(name='feature',
                             shape=((self.total_batches, self.batch_size) + feature.shape[1:]),
                             dtype=np.single)
            f.create_dataset(name='truth',
                             shape=((self.total_batches, self.batch_size) + truth.shape[1:]),
                             dtype=np.single)

    def __len__(self):
        """Denotes the number of batches per epoch"""
        return self.total_batches

    def __getitem__(self, batch_index: int):
        """Generate one batch of data"""
        with self.fetching:
            if batch_index not in self.cache_line:
                self.add_data_to_cache(batch_index)

            with h5py.File(self.cache_file, 'r') as f:
                return f['feature'][batch_index], f['truth'][batch_index]

    def on_epoch_end(self):
        """Modification of dataset between epochs"""
        if self.shuffle:
            random.shuffle(self.mixid)
            self.initialize_mixtures()

    def get_feature_frames(self, mixtures: list, mixid: Union[str, List[int]] = ':', start_offset: int = 0) -> int:
        subset = get_mixtures_from_mixid(mixtures, mixid)
        return sum([sub['samples'] for sub in subset]) // self.mixdb['feature_step_samples'] - start_offset

    def initialize_mixtures(self):
        self.mixdb['mixtures'] = get_mixtures_from_mixid(self.mixdb['mixtures'], self.mixid)

        frames = self.get_feature_frames(self.mixdb['mixtures'])
        self.frames_per_batch = self.batch_size if self.timesteps == 0 else self.batch_size * self.timesteps
        self.total_batches = frames // self.frames_per_batch

        if self.total_batches == 0:
            logger.error(
                f'Error: dataset only contains {frames} frames which is not enough to fill a batch size of '
                f'{self.frames_per_batch}. Either provide more data or decrease the batch size')
            raise SonusAIError

        # Compute mixid and offset for dataset
        # offsets are needed because mixtures are not guaranteed to fall on batch boundaries.
        # When fetching a new index that starts in the middle of a sequence of mixtures, the
        # previous feature frame offset must be maintained in order to preserve the correct
        # data sequence.
        self.index_map = list()
        cumulative_frames = 0
        start_mixture_index = 0
        offset = 0
        for mixture_index in range(len(self.mixdb['mixtures'])):
            current_frames = self.mixdb['mixtures'][mixture_index]['samples'] // self.mixdb['feature_step_samples']
            cumulative_frames += current_frames
            while cumulative_frames >= self.frames_per_batch:
                self.index_map.append({
                    'mixid':  list(range(start_mixture_index, mixture_index + 1)),
                    'offset': offset
                })
                extra_frames = cumulative_frames - self.frames_per_batch
                if extra_frames == 0:
                    start_mixture_index = mixture_index + 1
                    offset = 0
                else:
                    start_mixture_index = mixture_index
                    offset = current_frames - extra_frames
                cumulative_frames = extra_frames

    def add_data_to_cache(self, batch_index: int) -> None:
        # Don't skip any indices when filling cache
        if self.cache_line:
            next_cached_index = max(self.cache_line) + 1
            if batch_index > next_cached_index:
                batch_index = next_cached_index

        # Always fetch starting at a chunk boundary
        batch_index = (batch_index // self.chunks) * self.chunks

        mixid = self.index_map[batch_index]['mixid']
        offset = self.index_map[batch_index]['offset']
        chunks = self.get_feature_frames(mixtures=self.mixdb['mixtures'],
                                         mixid=mixid,
                                         start_offset=offset) // self.frames_per_batch
        while chunks < self.chunks and mixid[-1] < len(self.mixdb['mixtures']) - 1:
            mixid.append(mixid[-1] + 1)
            chunks = self.get_feature_frames(mixtures=self.mixdb['mixtures'],
                                             mixid=mixid,
                                             start_offset=offset) // self.frames_per_batch

        feature, truth, _, _ = genft(mixdb=self.mixdb,
                                     mixid=mixid,
                                     logging=False,
                                     parallel=False)

        feature = feature[offset:]
        truth = truth[offset:]

        frames = (feature.shape[0] // self.frames_per_batch) * self.frames_per_batch
        batches = frames // self.frames_per_batch

        if batches == 0:
            logger.error(
                f'Error: genft returned {feature.shape[0]} frames which is not enough to fill a batch size of '
                f'{self.frames_per_batch}. Either provide more data or decrease the batch size')
            raise SonusAIError

        feature = feature[:frames].reshape((batches, self.frames_per_batch, feature.shape[1], feature.shape[2]))
        truth = truth[:frames].reshape((batches, self.frames_per_batch, truth.shape[1]))

        # Add new values to cache file
        with h5py.File(self.cache_file, 'a') as f:
            for index in range(batches):
                self.cache_line.append(batch_index + index)
                new_feature, new_truth, _, _, _, _ = reshape_inputs(feature=feature[index],
                                                                    truth=truth[index],
                                                                    batch_size=self.batch_size,
                                                                    timesteps=self.timesteps,
                                                                    flatten=self.flatten,
                                                                    add1ch=self.add1ch)

                feature_dataset = f['feature']
                feature_dataset[batch_index + index] = new_feature

                truth_dataset = f['truth']
                truth_dataset[batch_index + index] = new_truth
