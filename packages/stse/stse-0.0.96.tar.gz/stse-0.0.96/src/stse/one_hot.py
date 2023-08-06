import numpy as np


def bit_vect(length, indices):
    """Generates a bit vector, hot at each index.

    Args:
        length (int): Length of desired bit vector.
        length
        indices (iter(int)): List of indices to equal 1.

    Returns:
        np.array: bit vector.
    """
    out = np.zeros(length)
    out[indices] = 1
    return out

def remove_hot_overlap(hot_vect, overlap_vect):
    overlap_vect = overlap_vect.astype(bool)
    hot_vect[overlap_vect] = 0
    return hot_vect
