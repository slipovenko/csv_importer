from abc import ABC


class BaseExporter(ABC):
    """
    Base exporter class. All exporters inherit from this one
    """
    def __init__(self, dest):
        """
        :param dest: Export destination
        """
        self.dest = dest
