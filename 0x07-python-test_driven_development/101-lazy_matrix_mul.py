#!/usr/bin/python3
def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    if len(m_a) == len(m_b):
        return np.matmul(m_a, m_b)
    else:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.dot(a, b)

