import unittest
from importers.csv_importer import CSVImporterBank1, CSVImporterBank2, CSVImporterBank3, BankCSVRecord
from importers.fabric import get_importer
from utils.exceptions import ImporterTypeError, RecordFormatError
from uuid import uuid4


class TestImporter(unittest.TestCase):

    def setUp(self) -> None:
        self.record_data = [
            {"format": "{time},{from}", "repr": "time,from", "data": {"time": "time", "from": "from"}},
            {"format": "{to},{from}", "repr": "to,from", "data": {"to": "to", "from": "from"}},
            {"format": "{amount},{from}", "repr": "100,from", "data": {"amount": 100, "from": "from"}},
            {"format": "{amount}", "repr": "100", "data": {"amount": 100, "from": "from"}},
        ]
        self.file_importer_list = {
            "data/bank1.csv": CSVImporterBank1,
            "data/bank2.csv": CSVImporterBank2,
            "data/bank3.csv": CSVImporterBank3,
        }

    def test_csv_record_dict(self):
        for record_dict in self.record_data:
            self.assertEqual(BankCSVRecord(**record_dict["data"]).dict_values, record_dict["data"])

    def test_csv_record_string_format(self):
        for record_dict in self.record_data:
            self.assertEqual(BankCSVRecord(**record_dict["data"]).get_formatted_record(record_dict["format"]),
                             record_dict["repr"])

    def test_csv_record_string_format_error(self):
        with self.assertRaises(RecordFormatError):
            BankCSVRecord(**{"name": "name"}).get_formatted_record()

    def test_csv_import_file_check_len(self):
        for filepath, importer in self.file_importer_list.items():
            rows_count = -1  # Excluding headers
            with open(filepath) as f:
                for line in f:
                    if line != "\n":
                        rows_count += 1
            data = importer(filepath).read_data()
            self.assertEqual(len(data), rows_count)

    def test_csv_import_file_check_type(self):
        for filepath, importer in self.file_importer_list.items():
            data = importer(filepath).read_data()
            for record in data:
                self.assertIsInstance(record, BankCSVRecord)

    def test_csv_import_file_check_format(self):
        for filepath, importer in self.file_importer_list.items():
            data = importer(filepath).read_data()
            check_record = data[0]
            for record in data:
                self.assertSequenceEqual(record.dict_values.keys(), check_record.dict_values.keys())

    def tearDown(self) -> None:
        self.record_data = None
        self.file_list = None
