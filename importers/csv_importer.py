from abc import abstractmethod
from csv import DictReader
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List
from collections import defaultdict
from utils.exceptions import (ImporterError, ImporterSourceError,
                              ImporterSourceFormatError, RecordFormatError)

from .base import BaseImporter, BaseRecord


@dataclass
class BankCSVRecord(BaseRecord):
    """
    Bank dataclass record
    """
    def __init__(self, **kwargs: Any):
        """
        Tricky init for any number and types of fields
        :param kwargs:
        """
        for name, value in kwargs.items():
            setattr(self, name, value)

    def get_formatted_record(self, record_format: str = None) -> str:
        """
        Returns string repr of record according to format. If substitute is not present in format it is ignored
        :param record_format:
        :return str
        """
        if record_format:
            return record_format.format_map(defaultdict(str, **self.dict_values))
        raise RecordFormatError("Format string must be set")

    @property
    def dict_values(self):
        """
        Property to get dict of dataclass fields
        :return: dict
        """
        return self.__dict__


class BaseCSVImporter(BaseImporter):
    @abstractmethod
    def read_data(self) -> List[BaseRecord]:
        """
        Abstract method for reading data from source
        """
        pass


class CSVImporterBank1(BaseCSVImporter):
    def read_data(self) -> List[BankCSVRecord]:
        """
        Reading data from csv file and creating list of data records
        :return: List of data records
        """
        try:
            with open(self.source, "r") as csv_source:
                row_records = []
                reader = DictReader(csv_source)
                for row in reader:
                    transformed_data = {
                        "timestamp": datetime.strptime(row["timestamp"], "%b %d %Y"),
                        "trans_type": row["type"],
                        "amount": row["amount"],
                        "from": row["from"],
                        "to": row["to"],
                    }
                    row_records.append(BankCSVRecord(**transformed_data))
                return row_records
        except FileNotFoundError as e:
            raise ImporterSourceError(message=f"File {self.source} not found")
        except KeyError as e:
            raise ImporterSourceFormatError(
                message="Source file data does not match format"
            )
        except Exception as e:
            raise ImporterError(message="Import failed!") from e


class CSVImporterBank2(BaseCSVImporter):
    def read_data(self) -> List[BankCSVRecord]:
        """
        Reading data from csv file and creating list of data records
        :return: List of data records
        """
        try:
            with open(self.source, "r") as csv_source:
                row_records = []
                reader = DictReader(csv_source)
                for row in reader:
                    transformed_data = {
                        "timestamp": datetime.strptime(row["date"], "%d-%m-%Y"),
                        "trans_type": row["transaction"],
                        "amount": row["amounts"],
                        "from": row["from"],
                        "to": row["to"],
                    }
                    row_records.append(BankCSVRecord(**transformed_data))
                return row_records
        except FileNotFoundError as e:
            raise ImporterSourceError(message=f"File {self.source} not found")
        except KeyError as e:
            raise ImporterSourceFormatError(
                message="Source file data does not match format"
            )
        except Exception as e:
            raise ImporterError(message="Import failed!") from e


class CSVImporterBank3(BaseCSVImporter):
    def read_data(self) -> List[BankCSVRecord]:
        """
        Reading data from csv file and creating list of data records
        :return: List of data records
        """
        try:
            with open(self.source, "r") as csv_source:
                row_records = []
                reader = DictReader(csv_source)
                for row in reader:
                    transformed_data = {
                        "timestamp": datetime.strptime(
                            row["date_readable"], "%d %b %Y"
                        ),
                        "trans_type": row["type"],
                        "amount": int(row["euro"]) + int(row["cents"]) / 100,
                        "from": row["from"],
                        "to": row["to"],
                    }
                    row_records.append(BankCSVRecord(**transformed_data))
                return row_records
        except FileNotFoundError as e:
            raise ImporterSourceError(message=f"File {self.source} not found")
        except KeyError as e:
            raise ImporterSourceFormatError(
                message="Source file data does not match format"
            )
        except Exception as e:
            raise ImporterError(message="Import failed!") from e
