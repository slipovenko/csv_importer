import unittest
from csv import DictReader

from exporters.csv_exporter import CSVBankExporter
from importers.csv_importer import CSVImporterBank1, CSVImporterBank2, CSVImporterBank3
from utils.exceptions import ExporterDestError, ExporterSettingsError


class TestExporter(unittest.TestCase):

    def setUp(self) -> None:

        files_and_importers = [
            ("data/bank1.csv", CSVImporterBank1),
            ("data/bank2.csv", CSVImporterBank2),
            ("data/bank3.csv", CSVImporterBank3)
        ]

        self.export_dest = "data/bank_common.csv"

        self.records = []
        for path, Importer in files_and_importers:
            self.records.extend(Importer(path).read_data())

    def test_csv_export_len(self):
        bank_exporter = CSVBankExporter(dest=self.export_dest)
        bank_exporter.export_data(self.records)

        rows_count = -1  # Excluding header
        with open(self.export_dest, "r") as result:
            for line in result:
                if line != "\n":
                    rows_count += 1
        self.assertEqual(rows_count, len(self.records))

    def test_csv_export_sum(self):
        records_amount_sum = sum(float(record.amount) for record in self.records)

        bank_exporter = CSVBankExporter(dest=self.export_dest)
        bank_exporter.export_data(self.records)
        with open(self.export_dest, "r") as result:
            reader = DictReader(result)
            result_amount_sum = sum(float(row["amount"]) for row in reader)
        self.assertEqual(records_amount_sum, result_amount_sum)

    def test_csv_export_source_error(self):
        with self.assertRaises(ExporterDestError):
            bank_exporter = CSVBankExporter(dest="folder_not_exists/ad4/")
            bank_exporter.export_data(self.records, [])

    def test_csv_export_settings_error(self):
        with self.assertRaises(ExporterSettingsError):
            bank_exporter = CSVBankExporter(dest=self.export_dest)
            bank_exporter.export_data(self.records, True)

    def tearDown(self) -> None:
        pass
