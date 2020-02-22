from pathlib import Path
import sys
class RootLocation:
    def __init__(self):
        self._script_run      = sys.argv[0]
        self._script_location = self.getFileName(0)
        self._script_name     = self.getFileName(1)
    def getFileName(self, file_or_path = 1):
        return Path(self._script_run).name if file_or_path == 1 else Path(self._script_run).parent
