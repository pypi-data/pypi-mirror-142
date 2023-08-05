import numpy as np
from pyaaware import ForwardTransform

from sonusai.utils import int16_to_float


def generate_segsnr(mixdb: dict,
                    record: dict,
                    target: np.ndarray,
                    noise: np.ndarray,
                    compute: bool = True,
                    frame_based: bool = False) -> np.ndarray:
    if not compute:
        return np.empty(0, dtype=np.single)

    fft = ForwardTransform(N=mixdb['frame_size'] * 4, R=mixdb['frame_size'])

    if frame_based:
        segsnr = np.empty(record['samples'] // mixdb['frame_size'], dtype=np.single)
    else:
        segsnr = np.empty(record['samples'], dtype=np.single)

    frame = 0
    for offset in range(0, record['samples'], mixdb['frame_size']):
        indices = slice(offset, offset + mixdb['frame_size'])
        target_energy = fft.energy(int16_to_float(target[indices]))
        noise_energy = fft.energy(int16_to_float(noise[indices]))
        if frame_based:
            segsnr[frame] = np.single(target_energy / noise_energy)
            frame += 1
        else:
            segsnr[indices] = np.single(target_energy / noise_energy)

    return segsnr
