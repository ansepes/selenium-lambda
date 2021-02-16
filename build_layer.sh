#!/bin/bash

CHROME_TOP="./headless"
CHROME_DL_DIR=$CHROME_TOP"/python"
CHROME_DIR=$CHROME_DL_DIR"/bin"
CHROME_ZIP="headless.zip"

rm -rf $CHROME_TOP
rm -rf $CHROME_ZIP
mkdir -p $CHROME_DIR

cd $CHROME_DL_DIR

wget https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip
unzip stable-headless-chromium-amazonlinux-2017-03.zip -d bin/
# wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d bin/

rm stable-headless-chromium-amazonlinux-2017-03.zip
rm chromedriver_linux64.zip

cd ../../

zip -r $CHROME_ZIP $CHROME_TOP

SELENIUM_TOP="./selenium"
SELENIUM_DIR=$SELENIUM_TOP"/python"
SELENIUM_ZIP="selenium.zip"
CRED_FILE="./credentials/secret.json"

rm -rf $SELENIUM_TOP
rm -rf $SELENIUM_ZIP
mkdir -p $SELENIUM_DIR

pip install --requirement ./requirements.txt -t $SELENIUM_DIR
# pip install selenium -t $SELENIUM_DIR

cp $CRED_FILE $SELENIUM_DIR

cd $SELENIUM_TOP

zip -r $SELENIUM_ZIP "./python"

mv $SELENIUM_ZIP ../