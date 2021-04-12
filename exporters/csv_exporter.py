from abc import abstractmethod
from csv import DictWriter
from typing import Any, List

from importers.csv_importer import BankCSVRecord
from utils.exceptions import (ExporterError, ExporterSettingsError,
                              ExporterDestError)

from .base import BaseExporter


class BaseCSVExporter(BaseExporter):
    @abstractmethod
    def export_data(self, data: List[BankCSVRecord], field_list: List):
        pass


class CSVBankExporter(BaseCSVExporter):
    """
    Exporter of Banking data to csv
    """
    def export_data(self, data: List[BankCSVRecord], field_list: List = None):
        """
        Produces csv file with transformed and formatted banking data
        :param data: List of Records to be imported to destination csv file
        :param field_list: List of fields to act as headers in csv file
        """
        try:
            if field_list:
                try:
                    iter(field_list)
                except TypeError as e:
                    raise ExporterSettingsError(message="Field list must be Iterable") from e
            else:
                field_list = data[0].dict_values.keys()
            with open(self.dest, "w") as csv_dest:
                writer = DictWriter(csv_dest, field_list, extrasaction="ignore")
                writer.writeheader()
                for record in data:
                    writer.writerow(record.dict_values)
        except FileNotFoundError as e:
            raise ExporterDestError(message=f"File {self.dest} not found") from e
