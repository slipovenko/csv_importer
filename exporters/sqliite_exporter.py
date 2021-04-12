from typing import Any, List

from .base import BaseExporter


class SQLiteExporter(BaseExporter):
    """
    Template exporter of data to SQLite
    """
    def export_data(self, data: List[Any]):
        """
        Exports data to sqlite
        :param data: List of object to be exported to xml
        """
        pass
