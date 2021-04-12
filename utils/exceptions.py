class ImporterError(Exception):
    def __init__(self, message):
        self.message = message


class ImporterTypeError(ImporterError):
    pass


class ImporterSettingsError(ImporterError):
    pass


class ImporterSourceError(ImporterError):
    pass


class ImporterSourceFormatError(ImporterError):
    pass


class RecordFormatError(ImporterError):
    pass


class ExporterError(Exception):
    def __init__(self, message):
        self.message = message


class ExporterTypeError(ExporterError):
    pass


class ExporterSettingsError(ExporterError):
    pass


class ExporterDestError(ExporterError):
    pass


class ExporterSourceFormatError(ExporterError):
    pass
