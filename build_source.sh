#!/bin/bash

SOURCE_ZIP="lambda.zip"
ENTRY_FILE="./lambda_function.py"
UTILS_DIR="./utils"

rm -rf $SOURCE_ZIP

zip -r $SOURCE_ZIP $ENTRY_FILE $UTILS_DIR