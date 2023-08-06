import numpy as np


def bit_vect(length, indices):
    """Generates a bit vector, hot at each index and 0 everywhere else.

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

