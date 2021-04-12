from typing import Type, Union

from .csv_exporter import CSVBankExporter
from .sqliite_exporter import SQLiteExporter
from utils.exceptions import ExporterTypeError

EXPORTERS = {
    "csv_bank": CSVBankExporter,
    "sqlite": SQLiteExporter,
}


def get_exporter(
        exporter_type: str, custom_exporter_dict: dict = None
) -> Type[
    Union[
        CSVBankExporter
    ]
]:
    """
    Returns exporter class by string exporter_type
    :param custom_exporter_dict: Custom set of exporters
    :param export_type: type for class to be returned
    :return: class
    """
    try:
        exporters = custom_exporter_dict or EXPORTERS
        return exporters[exporter_type]
    except KeyError as e:
        raise ExporterTypeError(f"Could not find Exporter for key={exporter_type}") from e
