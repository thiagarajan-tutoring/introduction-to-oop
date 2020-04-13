class Database:
    def __init__(self):
        raise NotImplementedError('Delete this once implemented.')

    def add(self, rows):
        """Adds `rows` to the database.

        Args:
            rows (List[List[*]]): list of rows to add to the table
        """
        raise NotImplementedError('Delete this once implemented.')

    def set_column_type(self, column_index, new_type):
        """Sets the column type for column `column_index` to `new_type`.

        Args:
            column_index (int): column index to change the type for
            new_type (any): type to change to (e.g. str, int, float)
        """
        raise NotImplementedError('Delete this once implemented.')

    def query(self, select_query, where_query=None):
        """Selects rows from a table conforming to `select_query` and `where_query`.

        Args:
            select_query (str): which columns to select (e.g. '*', '0,2', etc.)
            where_query (Any -> bool, optional): Boolean function for any row. Defaults to None.

        Returns:
            List corresponding to query results
        """
        raise NotImplementedError('Delete this once implemented.')

    def __repr__(self):
        raise NotImplementedError('Delete this once implemented.')


class GroupingDatabase(Database):
    def group(self, column_index):
        """Group the rows in the database by `column_index`

        Args:
            column_index (int): index to group database by

        Example: consider a database with rows
        [
            ['asdf', 1, 2],
            ['asdf', 2, 3],
            ['b', 1, 3]
        ]
        Grouping by column index 0 will modify the underlying table to be
        [
            ['asdf', [1, 2], [2, 3]],
            ['b', [1], [3]]
        ]
        Note that the last row in the grouped table still has the singleton values in lists.
        """
        raise NotImplementedError('Delete this once implemented.')

    def any(self, column_index, condition):
        """Checks if any row in table satisfies `condition` for `column_index`

        Args:
            column_index (int): index to validate
            condition (Any -> bool): boolean function to verify
        Returns:
            boolean: whether `condition` is satisfied at least once for a row at `column_index`
        """
        raise NotImplementedError('Delete this once implemented.')

    def all(self, column_index, condition):
        """Checks if all rows in table satisfies `condition` for `column_index`

        Args:
            column_index (int): index to validate
            condition (Any -> bool): boolean function to verify
        Returns:
            boolean: whether `condition` is satisfied for all rows or not at `column_index`
        """
        raise NotImplementedError('Delete this once implemented.')

    def sum(self, column_index):
        """Sums column `column_index` over all rows in the database

        Args:
            column_index (int): column to sum over
        Returns:
            Any: the sum over the column `column_index` in the database
        Note:
            the sum does not necessarily have to be with ints. For example, summing lists should
            return all lists concatenated
        """
        raise NotImplementedError('Delete this once implemented.')

if __name__ == '__main__':
    db = Database()
    db.add([['asdf', 1, 3]])
    db.add([['asdf', 1, 3]])
    db.set_column_type(1, str)
    print(
        db.query('0,2', lambda row: row[2] == 3)
    )
    print(db)
    gdb = GroupingDatabase()
    gdb.add([['asdf', 1, 3]])
    gdb.add([['asdf', 1, 3]])
    gdb.set_column_type(1, str)
    print(
        gdb.query('0,2', lambda row: row[2] == 3)
    )
    print(gdb)
    print('any', gdb.any(0, lambda row: row == 'a'))
    print('all', gdb.all(2, lambda row: row == 3))
    gdb.group(1)
    print(gdb)
