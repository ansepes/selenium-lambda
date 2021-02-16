from utils.selenium_util import SeleniumUtil


def lambda_handler(event, context):
  selenium = None
  try:
    selenium = SeleniumUtil()

    # - ドライバーの初期化
    selenium.build_pc_driver()

    # page = LoginPagePC(selenium)
    # page.open()
    # # print(selenium.driver().current_url)
    # return selenium.driver().current_url
    selenium.driver().get("https://www.google.co.jp")
    result = {
        'statusCode': 200,
        'body': selenium.driver().title
    }

    return result
  finally:
    if selenium:
      selenium.dispose_driver()
