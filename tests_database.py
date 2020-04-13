#!/usr/bin/env python3
import pytest


def test_database_add():
    from database import Database
    db = Database()
    with pytest.raises(Exception) as _:
        db.add([2])
    db.add([[1, 'asdf', True]])
    with pytest.raises(Exception) as _:
        db.add([[2]])
    with pytest.raises(Exception) as _:  
        db.add(['asdf', 1, False])


def test_database_set_column_type():
    from database import Database
    db = Database()
    db.add([[1, 'asdf', True]])
    db.set_column_type(0, str)
    db.set_column_type(2, int)


def test_database_query():
    from database import Database
    db = Database()
    db.add([[1, 'asdf', True]])
    db.add([[2, 'fdsa', False]])
    query_result = db.query('*', where_query=lambda row: row[2])
    assert len(query_result) == 1
    assert query_result[0][0] == 1 and query_result[0][1] == 'asdf'
    query_result = db.query('0,2', where_query=lambda row: row[0] == 2)
    assert len(query_result) == 1
    assert query_result[0][0] == 2 and len(query_result[0]) == 2 and not query_result[0][1]


def test_grouping_database_group():
    from database import GroupingDatabase
    db = GroupingDatabase()
    db.add([[1, 'asdf', True]])
    db.add([[1, 'fdsa', False]])
    db.group(0)
    query_result = db.query('*')
    assert len(query_result) == 1
    assert query_result[0][0] == 1 and len(query_result[0][1]) == 2 and len(query_result[0][2]) == 2


def test_grouping_database_any():
    from database import GroupingDatabase
    db = GroupingDatabase()
    db.add([[1, 'asdf', True]])
    db.add([[1, 'fdsa', False]])
    assert db.any(2, lambda col: col)
    db.group(0)
    assert db.any(1, lambda col: 'asdf' in col)


def test_grouping_database_all():
    from database import GroupingDatabase
    db = GroupingDatabase()
    db.add([[1, 'asdf', True]])
    db.add([[1, 'fdsa', False]])
    db.add([[1, 'adsf', False]])
    assert db.all(0, lambda col: col == 1)
    db.group(0)
    assert db.all(1, lambda col: 'asdf' in col)


def test_grouping_database_sum():
    from database import GroupingDatabase
    db = GroupingDatabase()
    db.add([[1, 10, 'asdf']])
    db.add([[1, 5, 'asdf']])
    db.add([[2, 3, 'fdsa']])
    assert db.sum(1) == 18
    db.group(0)
    assert db.sum(1) == [10, 5, 3]
