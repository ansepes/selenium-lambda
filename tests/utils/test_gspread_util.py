
from utils.gspread_util import GSpreadUtil


class TestGSpreadUtil:

  def test_read_value(self):
    spread_util = GSpreadUtil()
    value = spread_util.read_value('同日スイッチ', 'B10')
    print(value)
