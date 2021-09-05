# selenium-lambda

## 環境構築
- build_layer.shを実行する
    - headless chromeがセットアップされる
- 作業ディレクトリのパス等の環境変数を設定する
    - pytest用：conf/test_env.json
    - 手動実行用：.devcontainer/devcontainer.json
- GoogleSpreadsheetを使用する場合
    - credentials/secret.jsonを配置する