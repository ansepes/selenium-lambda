from conf.config import Config
from oauth2client.service_account import ServiceAccountCredentials
import gspread


class GSpreadUtil:
  def __init__(self) -> None:
    config = Config()

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(config.CRED_FILE, scope)
    gc = gspread.authorize(credentials)
    self._workbook = gc.open_by_key(config.SPREADSHEET_KEY)

  def read_value(self, sheet_name: str, a1: str) -> str:
    ws = self._workbook.worksheet(sheet_name)
    cell = ws.acell(a1)
    return cell.value
