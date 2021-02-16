
from lambda_function import lambda_handler


class TestLambdaFunction:

  def test_handler(self):
    result = lambda_handler({}, {})
    print(result)
    assert result['body'] == 'Google'
