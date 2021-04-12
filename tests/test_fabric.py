import unittest
from importers.csv_importer import CSVImporterBank1, CSVImporterBank2, CSVImporterBank3
from exporters.csv_exporter import CSVBankExporter
from exporters.fabric import get_exporter
from importers.fabric import get_importer
from utils.exceptions import ImporterTypeError, ExporterTypeError
from uuid import uuid4


class TestImportFabric(unittest.TestCase):

    def setUp(self) -> None:
        self.importers = {
            "csv_bank1": CSVImporterBank1,
            "csv_bank2": CSVImporterBank2,
            "csv_bank3": CSVImporterBank3,
        }

    def test_fabric_imorter_exists(self):
        for importer_type in self.importers.keys():
            assert self.importers[importer_type] == get_importer(importer_type)

    def test_fabric_imorter_exists_custom(self):
        for importer_type in self.importers.keys():
            assert self.importers[importer_type] == get_importer(importer_type, self.importers)

    def test_fabris_error(self):
        with self.assertRaises(ImporterTypeError):
            get_importer(uuid4())

    def tearDown(self) -> None:
        self.importers = None


class TestExportFabric(unittest.TestCase):

    def setUp(self) -> None:
        self.exporters = {
            "csv_bank": CSVBankExporter,
        }

    def test_fabric_exporter_exists(self):
        for exporter_type in self.exporters.keys():
            assert self.exporters[exporter_type] == get_exporter(exporter_type, self.exporters)

    def test_fabric_exporter_exists_custom(self):
        for exporter_type in self.exporters.keys():
            assert self.exporters[exporter_type] == get_exporter(exporter_type)

    def test_fabris_error(self):
        with self.assertRaises(ExporterTypeError):
            get_exporter(uuid4())

    def tearDown(self) -> None:
        self.importers = None
