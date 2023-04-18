from WorkerSignals import WorkerSignals
from PySide6.QtCore import QRunnable, Slot
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

class Worker(QRunnable):

    def __init__(self, instance, method, *args, **kwargs):
        super(Worker, self).__init__()
        self.instance = instance
        self.method = method
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        logging.debug(f"running method: {self.method}")
        result = None
        try:
            method = getattr(self.instance, self.method.__name__)
            result = method(*self.args, **self.kwargs)
            if result is None:
                result = "" # the method doesn't return anything, but no error was found so we return an empty string
        except Exception as e: 
            logging.exception(e)
            logging.error(f"Error trying to execute worker for method {self.method}. See above logs to debug issue.")
        self.signals.result.emit(result)
