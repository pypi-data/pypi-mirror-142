import json
import pandas as pd
import pandas.api.types as pdt
from hopara import Table, ColumnType


def get_rows(df: pd.DataFrame) -> dict:
    """Get rows in Hopara format from a Pandas df.
    :param df: a DataFrame from pandas library.
    :type df: pandas.DataFrame
    :return: rows in Hopara format
    :rtype: list of dicts
    """
    return json.loads(df.to_json(orient="records", date_format='iso'))


def get_table(table_name: str, df: pd.DataFrame) -> Table:
    """Generate a Hopara Table from a Pandas df.
    This function is able to detect the most common types, but for some complex types it can't.
    In these cases you can set by yourself on the Table object calling the ``set_column_types`` function.

    Auto-detected types
     - ``STRING``, ``INTEGER``, ``DECIMAL``, ``BOOLEAN``
     - ``DATETIME``: python datetime format

    :param table_name: table name
    :type table_name: str
    :param df: pandas DataFrame
    :type df: pandas.DataFrame
    :return: Table generated based on pandas DataFrame
    :rtype: hopara.Table
    """
    table = Table(table_name)
    for column_name in df.columns:
        column_type = None
        if pdt.is_float_dtype(df[column_name]):
            column_type = ColumnType.DECIMAL
        elif pdt.is_integer_dtype(df[column_name]):
            column_type = ColumnType.INTEGER
        elif pdt.is_bool_dtype(df[column_name]):
            column_type = ColumnType.BOOLEAN
        elif column_name in ['_geo_json']:
            column_type = ColumnType.JSON
        elif column_name in ['_contour']:
            column_type = ColumnType.POLYGON
        elif pdt.is_string_dtype(df[column_name]):
            column_type = ColumnType.STRING
        elif pdt.is_datetime64_dtype(df[column_name]):
            column_type = ColumnType.DATETIME
        table.add_column(column_name, column_type)
    return table

