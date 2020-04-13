#!/usr/bin/env python3
import pytest


def test_vector_setup():
    from matrix import Vector
    v_1 = Vector(3)
    v_1[0] = 5
    v_1[2] = -3
    assert str(v_1) == '[5, 0, -3]'
    v_2 = Vector(3, value=[2, 1, 3])
    assert v_2[0] == 2 and v_2[1] == 1 and v_2[2] == 3
    with pytest.raises(Exception) as _:
        _ = Vector(4, value=[2, 1, 3])


def test_vector_add():
    from matrix import Vector
    v_1 = Vector(3)
    v_1[0] = 5
    v_1[2] = -3
    v_bad = Vector(4, value=[2, 1, 3, 4])
    with pytest.raises(Exception) as _:
        _ = Vector.add(v_1, v_bad)
    v_2 = Vector(3, value=[-5, 0, 3])
    v_add = Vector.add(v_1, v_2)
    assert v_add[0] == 0 and v_add[1] == 0 and v_add[2] == 0


def test_vector_dot():
    from matrix import Vector
    v_1 = Vector(3)
    v_1[0] = 5
    v_1[2] = -3
    v_bad = Vector(4, value=[2, 1, 3, 4])
    with pytest.raises(Exception) as _:
        _ = Vector.dot(v_1, v_bad)
    v_2 = Vector(3, value=[-5, 0, 3])
    v_dot = Vector.dot(v_1, v_2)
    assert v_dot == -34


def test_matrix_setup():
    from matrix import Matrix
    m_1 = Matrix((4, 3))
    m_1[0][1] = 2
    m_1.transpose()
    _ = Matrix((2, 2), value=[[1, 2], [3, 4]])


def test_matrix_transpose():
    from matrix import Matrix
    m_1 = Matrix((4, 3))
    m_1[0][1] = 2
    m_1.transpose()
    assert m_1[1][0] == 2


def test_matrix_add():
    from matrix import Matrix
    m_1 = Matrix((4, 3))
    m_1[0][1] = 2
    m_2 = Matrix((2, 2), value=[[1, 2], [3, 4]])
    with pytest.raises(Exception) as _:
        _ = Matrix.add(m_1, m_2)
    m_3 = Matrix((4, 3), value=[[1, 2, 3], [0, 2, 1], [4, 5, -1], [1, 2, 0]])
    m_add = Matrix.add(m_1, m_3)
    assert m_add[0][0] == 1
    assert m_add[0][1] == 4
    assert m_add[0][2] == 3


def test_matrix_dot():
    from matrix import Matrix
    m_1 = Matrix((4, 3))
    m_1[0][1] = 2
    m_2 = Matrix((2, 2), value=[[1, 2], [3, 4]])
    with pytest.raises(Exception) as _:
        _ = Matrix.dot(m_1, m_2)
    m_3 = Matrix((4, 3), value=[[1, 2, 3], [0, 2, 1], [4, 5, -1], [1, 2, 0]])
    m_3.transpose()
    m_dot = Matrix.dot(m_1, m_3)
    assert m_dot[0][0] == 4
    assert m_dot[0][1] == 4
    assert m_dot[0][2] == 10
    assert m_dot[0][3] == 4
