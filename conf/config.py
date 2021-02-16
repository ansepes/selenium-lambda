import os


class Singleton(object):
  def __new__(cls, *args, **kargs):
    if not hasattr(cls, "_instance"):
      cls._instance = super(Singleton, cls).__new__(cls)
    return cls._instance


class Config(Singleton):
  def __init__(self):
    if hasattr(self, '_initialized'):
      return
    self.__init_config()
    self._initialized = True

  def __init_config(self):
    # chrome base path
    pwd = os.getenv('PWD', default='')
    self.CHROME_BASE_PATH = pwd
    if self.__running_on_lambda():
      self.CHROME_BASE_PATH = '/opt'

    # gspread credential file path
    self.CRED_FILE = f'{pwd}/credentials/secret.json'
    if self.__running_on_lambda():
      self.CRED_FILE = '/opt/python/secret.json'

    # /credentials/env.json
    # gspread file key
    self.SPREADSHEET_KEY = os.getenv('SPREADSHEET_KEY', default='')

  def __running_on_lambda(self):
    if os.getenv('AWS_LAMBDA_RUNTIME_API', default=False):
      return True
    return False
