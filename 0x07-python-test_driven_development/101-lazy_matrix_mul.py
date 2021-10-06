#!/usr/bin/python3
"""Function lazy_matrix_mul multiply two matrix with numpy"""


def lazy_matrix_mul(m_a, m_b):
    """Args: m_a, m_b
        return multiply of two matrix
    """
    import numpy as np
    if len(m_a) == len(m_b):
        return np.matmul(m_a, m_b)
    else:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.dot(a, b)
