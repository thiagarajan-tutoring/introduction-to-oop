class Database:
    def __init__(self):
        self.underlying_list = []

    def add(self, rows):
        """Adds `rows` to the database.

        Args:
            rows (List[List[*]]): list of rows to add to the table
        """
        # Need to check that rows is a list of lists
        assert (type(rows) == list)
        for row in rows:
            assert (type(row) == list)

        # Need to check that number of columns for each row in rows is the same as the number of 
        # columns currently in the database (i.e. self.underlying_list)
        if len(self.underlying_list) > 0:
            num_cols = len(self.underlying_list[0])
            for row in rows:
                assert (len(row) == num_cols)

        # Need to check the type of each column being added in each row
        self.underlying_list.append(rows)

    def set_column_type(self, column_index, new_type):
        """Sets the column type for column `column_index` to `new_type`.

        Args:
            column_index (int): column index to change the type for
            new_type (any): type to change to (e.g. str, int, float)
        """
        for row in self.underlying_list:
            row[column_index] = new_type(row[column_index])

    def query(self, select_query, where_query=None):
        """Selects rows from a table conforming to `select_query` and `where_query`.

        Args:
            select_query (str): which columns to select (e.g. '*', '0,2', etc.)
            where_query (Any -> bool, optional): Boolean function for any row. Defaults to None.

        Returns:
            List corresponding to query results
        """
        # Process select query to get the desired columns (could be '*', or could be '0, 1, 2', etc.)
        if select_query == '*':
            # Set column indices to be all of them
        else:
            # Figure out how grab a list of integers corresponding to what's in select query
        # Figure out how to grab all the rows, but only selected columns, and put that into queried_rows
        queried_rows = ...  # The result of doing the select query
        output = []
        for row in queried_rows:
            if where_query(row):
                output.append(row)
        return output

    def __repr__(self):
        raise NotImplementedError('Delete this once implemented.')


class GroupingDatabase(Database):
    def group(self, column_index):
        """Group the rows in the database by `column_index`

        Args:
            column_index (int): index to group database by

        Example: consider a database with rows
        [
            ['asdf', 1, 3],
            ['asdf', 2, 4],
            ['b', 1, 3],
            ['b', 2, 4]
        ]
        Grouping by column index 0 will modify the underlying table to be
        [
            ['asdf', [1, 2], [3, 4]],
            ['b', [1, 2], [3, 4]]
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

        Example:
        [
            [1, 'asdf, 2],
            [2, 'b', 3]
        ]

        >> database_instance.any(1, lambda entry: entry == 'b')
        True
        >> database.instance.any(0, lambda entry: entry == 4)
        False
        """
        raise NotImplementedError('Delete this once implemented.')

    def all(self, column_index, condition):
        """Checks if all rows in table satisfies `condition` for `column_index`

        Args:
            column_index (int): index to validate
            condition (Any -> bool): boolean function to verify
        Returns:
            boolean: whether `condition` is satisfied for all rows or not at `column_index`

        Example:
        [
            [1, 'b', 2],
            [2, 'b', 3]
        ]

        >> database_instance.all(1, lambda entry: entry == 'b')
        True
        >> database.instance.all(0, lambda entry: entry == 1)
        False
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
        # Probably use the sum function native to Python
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
