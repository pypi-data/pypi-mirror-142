from dataclasses import dataclass
from typing import List


@dataclass
class Mixture:
    target_file_index: int
    noise_file_index: int
    noise_offset: int
    target_augmentation_index: int
    noise_augmentation_index: int
    target_snr_gain: float
    noise_snr_gain: float
    samples: int
    target_gain: float
    class_count: List[int]


@dataclass
class Noise:
    name: str
    duration: float


@dataclass
class Target:
    name: str
    duration: float
    truth_index: List[List[int]]
    truth_function: List[str]
    truth_config: List[dict]


@dataclass
class MixtureDatabase:
    class_count: List[int]
    class_labels: List[str]
    class_weights_threshold: List[float]
    dither: bool
    feature: str
    feature_samples: int
    feature_step_samples: int
    frame_size: int
    mixtures: dict
    noise_augmentations: List[dict]
    noises: List[Noise]
    num_classes: int
    target_augmentations: List[dict]
    targets: List[Target]
    truth_mutex: bool
    truth_reduction_function: str
