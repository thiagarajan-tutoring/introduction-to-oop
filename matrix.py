class Vector:
    def __init__(self, shape, value=None):
        """Initializes a vector with `shape` entries, and optionally with value `value`.

        Args:
            shape (int): number of entries
            value (List, optional): Value to initialize the vector with. Defaults to None.
        """
        raise NotImplementedError('Delete this once implemented.')

    def __getitem__(self, index):
        raise NotImplementedError('Delete this once implemented.')

    def __setitem__(self, index, value):
        raise NotImplementedError('Delete this once implemented.')

    def __repr__(self):
        raise NotImplementedError('Delete this once implemented.')

    @classmethod
    def add(cls, v_1, v_2):
        """Adds two vectors `v_1` and `v_2`.

        Args:
            v_1 (Vector)
            v_2 (Vector)

        Returns:
            Vector: The result of v_1 + v_2
        """
        raise NotImplementedError('Delete this once implemented.')

    @classmethod
    def dot(cls, v_1, v_2):
        """Takes the dot product of two vectors `v_1` and `v_2`.

        Args:
            v_1 (Vector)
            v_2 (Vector)

        Returns:
            Vector: The result of v_1 @ v_2, i.e. the dot product
        """
        raise NotImplementedError('Delete this once implemented.')


class Matrix(Vector):
    def __init__(self, shape, value=None):
        """Initializes a vector with `shape` dimensions, and optionally with value `value`.

        Args:
            shape (Tuple(int)): shape of the matrix
            value (List, optional): Value to initialize the vector with. Defaults to None.
        """
        raise NotImplementedError('Delete this once implemented.')

    def transpose(self):
        """Transposes the matrix instance."""
        raise NotImplementedError('Delete this once implemented.')

    @classmethod
    def add(cls, m_1, m_2):
        """Adds two matrices `m_1` and `m_2`.
        
        Args:
            m_1 (Matrix)
            m_2 (Matrix)
        
        Returns:
            Matrix: sum of `m_1` and `m_2`
        """
        raise NotImplementedError('Delete this once implemented.')

    @classmethod
    def dot(cls, m_1, m_2):
        """Returns the matrix-product of `m_1` and `m_2`.

        Args:
            m_1 (Matrix)
            m_2 (Matrix):

        Returns:
            Matrix: Result of `m_1` @ `m_2`
        """
        raise NotImplementedError('Delete this once implemented.')


if __name__ == '__main__':
    v_1 = Vector(3, value=[0, 4, 2])
    v_1[0] = 1
    v_2 = Vector(3, value=[1, 2, 3])
    print(Vector.add(v_1, v_2))
    print(Vector.dot(v_1, v_2))
    m_1 = Matrix((4, 3))
    m_1[0][0] = 3
    m_1[1][1] = 2
    m_1[2][2] = 5
    m_2 = Matrix(
        (3, 6), value=[[1] * 6, [2] * 6, [3] * 6]
    )
    print(Matrix.add(m_1, m_1))
    print(Matrix.dot(m_1, m_2), Matrix.dot(m_1, m_2).shape)
