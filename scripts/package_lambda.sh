#!/bin/bash

# Define variables
LAMBDA_DIR="src/lambda_function"
PACKAGE_NAME="lambda_function.zip"

# Navigate to the Lambda function directory
cd $LAMBDA_DIR

# Install dependencies
pip install -r requirements.txt -t .

# Package the Lambda function and its dependencies
zip -r ../$PACKAGE_NAME .

# Navigate back to the original directory
cd ../..