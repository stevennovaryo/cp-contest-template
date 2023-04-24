class ErrorHandler:
  
  file_path: str

  def init_fix_file(self, file_path: str):
    self.file_path = file_path
  
  def raise_error(self, error: Exception):
    print(f'[FAILED] on file {self.file_path}')
    raise error


class UnsupportedCaseStructure(Exception):
  def __init__(self, message):
    super().__init__(message)
