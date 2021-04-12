from typing import Type, Union

from utils.exceptions import ImporterTypeError

from .csv_importer import CSVImporterBank1, CSVImporterBank2, CSVImporterBank3
from .json_importer import JSONImporter
from .xml_importer import XMLImporter

IMPORTERS = {
    "csv_bank1": CSVImporterBank1,
    "csv_bank2": CSVImporterBank2,
    "csv_bank3": CSVImporterBank3,
    "xml": XMLImporter,
    "json": JSONImporter,
}


def get_importer(
        importer_type: str, custom_importer_dict: dict = None
) -> Type[
    Union[
        CSVImporterBank1, CSVImporterBank2, CSVImporterBank3, XMLImporter, JSONImporter
    ]
]:
    """
    Returns import class by string import_type
    :param custom_importer_dict: Custom set of importers
    :param import_type: type for class to be returned
    :return: class
    """
    try:
        importers = custom_importer_dict or IMPORTERS
        return importers[importer_type]
    except KeyError as e:
        raise ImporterTypeError(f"Could not find Importer for key={importer_type}") from e
