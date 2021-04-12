import logging as log

from exporters.fabric import get_exporter
from importers.fabric import get_importer
from utils.exceptions import ExporterError, ImporterError

if __name__ == "__main__":

    files_and_importers = [
        ("data/bank1.csv", get_importer("csv_bank1")),
        ("data/bank2.csv", get_importer("csv_bank2")),
        ("data/bank3.csv", get_importer("csv_bank3")),
    ]

    export_dest = "data/bank_common.csv"

    # Reading all the records from bank files. Appending to single list
    records = []
    try:
        for path, Importer in files_and_importers:
            log.warning(f"Importing data from {path}")
            records.extend(Importer(path).read_data())
            log.warning(f"Imported data from {path}")
    except ImporterError as e:
        log.error(e.message)

    if records:
        try:
            log.warning(f"Exporting {len(records)} rows to {export_dest}")
            Exporter = get_exporter("csv_bank")
            # Passing records list to the exporter
            bank_exporter = Exporter(dest="data/bank_common.csv")
            bank_exporter.export_data(records)
            log.warning(f"Exported {len(records)} rows to {export_dest}")
        except ExporterError as e:
            log.error(e.message)
    else:
        log.warning("No data was imported")
