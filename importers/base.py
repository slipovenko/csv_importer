from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseRecord:
    """
    Base dataclass for data record.
    """
    record_type: str

    @abstractmethod
    def get_formatted_record(self, record_format: str) -> Any:
        """
        Returns formatted repr of record according to format
        :param record_format:
        :return Any
        """
        pass


class BaseImporter:
    """
    Base Importer class
    """
    def __init__(self, source: Any):
        """
        :param source: Source of data. filepath/web source or any other
        """
        self.source = source
