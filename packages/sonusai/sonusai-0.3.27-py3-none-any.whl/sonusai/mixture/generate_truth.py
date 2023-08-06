from copy import deepcopy

import h5py
import numpy as np
from pyaaware import ForwardTransform
from pyaaware import SED

from sonusai import SonusAIError
from sonusai import logger
from sonusai.mixture import get_class_count
from sonusai.mixture import get_class_weights_threshold
from sonusai.utils import int16_to_float


def strictly_decreasing(list_to_check: list) -> bool:
    return all(x > y for x, y in zip(list_to_check, list_to_check[1:]))


def generate_truth(mixdb: dict,
                   record: dict,
                   target: np.ndarray,
                   noise: np.ndarray,
                   compute: bool = True) -> np.ndarray:
    if not compute:
        return np.empty(0, dtype=np.single)

    truth_config = deepcopy(mixdb['targets'][record['target_file_index']]['truth_config'])
    truth_config['frame_size'] = mixdb['frame_size']
    truth_config['num_classes'] = mixdb['num_classes']
    truth_config['mutex'] = mixdb['truth_mutex']
    truth_config['target_gain'] = record['target_gain']

    indices = mixdb['targets'][record['target_file_index']]['truth_index']
    functions = mixdb['targets'][record['target_file_index']]['truth_function']

    if len(functions) != len(indices):
        logger.error('length of truth_index does not match length of truth_function')
        raise SonusAIError

    truth = np.zeros((len(target), truth_config['num_classes']), dtype=np.single)
    for i in range(len(functions)):
        truth_config['function'] = functions[i]
        truth_config['index'] = indices[i]
        new_truth = truth_function(target=target,
                                   noise=noise,
                                   config=truth_config)
        truth = truth + new_truth

    record['class_count'] = get_class_count(
        truth_index=indices,
        truth=truth,
        class_weights_threshold=get_class_weights_threshold(mixdb))

    return truth


def truth_function(target: np.ndarray,
                   noise: np.ndarray,
                   config: dict) -> np.ndarray:
    if config['function'] == 'sed':
        if config['target_gain'] == 0:
            return np.zeros((len(target), config['num_classes']), dtype=np.single)

        if len(target) % config['frame_size'] != 0:
            logger.error(f'Number of samples in audio is not a multiple of {config["frame_size"]}')
            raise SonusAIError

        if 'thresholds' in config:
            thresholds = config['thresholds']
            if not isinstance(thresholds, list) or len(thresholds) != 3:
                logger.error(f'Truth function SED thresholds does not contain 3 entries: {thresholds}')
                raise SonusAIError
            if not strictly_decreasing(thresholds):
                logger.error(f'Truth function SED thresholds are not strictly decreasing: {thresholds}')
                raise SonusAIError
        else:
            thresholds = None

        fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])
        sed = SED(thresholds=thresholds,
                  index=config['index'],
                  frame_size=config['frame_size'],
                  num_classes=config['num_classes'],
                  mutex=config['mutex'])

        audio = np.int16(np.single(target) / config['target_gain'])
        truth = np.empty((0, config['num_classes']), dtype=np.single)
        for offset in range(0, len(audio), config['frame_size']):
            new_truth = sed.execute(fft.energy(int16_to_float(audio[offset:offset + config['frame_size']])))
            truth = np.vstack((truth, np.reshape(new_truth, (1, len(new_truth)))))

        truth = truth.repeat(config['frame_size'], axis=0)
        return truth

    elif config['function'] == 'file':
        file_parameters = ['file']
        for parameter in file_parameters:
            if parameter not in config:
                logger.error(f'Truth function config missing required parameter: {parameter}')
                raise SonusAIError

        with h5py.File(name=config['file'], mode='r') as f:
            truth_in = f['/truth_t'][:]

        if truth_in.ndim != 2:
            logger.error('Truth file data is not 2 dimensions')
            raise SonusAIError

        if truth_in.shape[0] != len(target):
            logger.error('Truth file does not contain the right amount of samples')
            raise SonusAIError

        truth = np.zeros((len(target), config['num_classes']), dtype=np.single)
        if config['target_gain'] == 0:
            return truth

        if isinstance(config['index'], list):
            if len(config['index']) != truth_in.shape[1]:
                print('Truth file does not contain the right amount of classes')
                raise SonusAIError

            truth[:, config['index']] = truth_in
        else:
            if config['index'] + truth_in.shape[1] > config['num_classes']:
                print('Truth file contains too many classes')
                raise SonusAIError

            truth[:, config['index']:config['index'] + truth_in.shape[1]] = truth_in

        return truth

    elif config['function'] == 'snr':
        truth = np.zeros((len(target), config['num_classes']), dtype=np.single)
        fft = ForwardTransform(N=config['frame_size'] * 4, R=config['frame_size'])
        for offset in range(0, len(target), config['frame_size']):
            target_energy = fft.energy(int16_to_float(target[offset:offset + config['frame_size']]))
            noise_energy = fft.energy(int16_to_float(noise[offset:offset + config['frame_size']]))
            truth[offset:offset + config['frame_size'], config['index']] = np.single(target_energy / noise_energy)

        return truth

    elif config['function'] == 'phoneme':
        # Read in .txt transcript and run a Python function to generate text grid data
        # (indicating which phonemes are active)
        # Then generate truth based on this data and put in the correct classes based on config['index']
        logger.error('phoneme function is not supported yet')
        raise SonusAIError

    logger.error(f'Unsupported truth function: {config["function"]}')
    raise SonusAIError
