from PySide6.QtCore import QObject, Signal

class WorkerSignals(QObject):
    finished = Signal()
    result = Signal(object)
