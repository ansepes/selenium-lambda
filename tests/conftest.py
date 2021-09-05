import json
import os
import pytest


@pytest.fixture(scope='session', autouse=True)
def cmdopt(request):
  """Get options value."""

  set_environment_variable('./conf/test_env.json')


def set_environment_variable(json_filepath):
  """Jsonを読み込み環境変数にセットする."""
  with open(f"./{json_filepath}") as filedata:
    for key, value in json.load(filedata).items():
      os.environ[key] = value
