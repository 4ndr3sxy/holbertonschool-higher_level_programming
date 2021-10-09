#!/usr/bin/python3
"""Function lazy_matrix_mul multiply two matrix with numpy"""


def lazy_matrix_mul(m_a, m_b):
    """Args: m_a, m_b
        return multiply of two matrix
    """
    import numpy as np

    for groupa in m_a, m_b:
        for j in groupa:
            if type(j) not in (int, float):
                return "Scalar operands are not allowed, use '*' instead"

    for groupb in m_b:
        for k in groupb:
            if type(k) not in (int, float):
                return "Scalar operands are not allowed, use '*' instead"
    if len(m_a) == len(m_b):
        return np.matmul(m_a, m_b)
    else:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.dot(a, b)
