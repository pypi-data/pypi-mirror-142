from typing import List

import numpy as np


def get_class_count(truth_index: List[List[int]],
                    truth: np.ndarray,
                    class_weights_threshold: List[float]) -> List[List[int]]:
    class_count = [[] for _ in range(len(truth_index))]
    for n in range(len(truth_index)):
        class_count[n] = [0] * len(truth_index[n])
        for idx, cl in enumerate(truth_index[n]):
            truth_sum = int(np.sum(truth[:, cl - 1] >= class_weights_threshold[cl - 1]))
            class_count[n][idx] = truth_sum

    return class_count


def get_total_class_count(mixdb: dict) -> List[int]:
    total_class_count = [0] * mixdb['num_classes']
    for mixture in mixdb['mixtures']:
        truth_indices = mixdb['targets'][mixture['target_file_index']]['truth_index']
        for n in range(len(truth_indices)):
            for idx, cl in enumerate(truth_indices[n]):
                total_class_count[cl - 1] += int(mixture['class_count'][n][idx])

    return total_class_count
