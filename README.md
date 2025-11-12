# AWS CI/CD Python Lambda Demo

This project demonstrates a simple AWS CI/CD pipeline using AWS CodePipeline, CodeBuild, and a Python Lambda function. The setup includes CloudFormation templates for deploying the necessary resources and a build specification for CodeBuild.

## Project Structure

```
aws-cicd-python-lambda-demo
├── src
│   └── lambda_function
│       ├── app.py               # Main Lambda function code
│       ├── requirements.txt      # Python dependencies
│       └── tests
│           └── test_app.py       # Unit tests for the Lambda function
├── infra
│   ├── lambda-template.yaml       # CloudFormation template for Lambda
│   ├── pipeline-template.yaml      # CloudFormation template for CodePipeline
│ 
├── codebuild
│   └── buildspec.yml             # Build specification for CodeBuild
├── scripts
│   └── package_lambda.sh          # Script to package Lambda function
├── .gitignore                     # Git ignore file
├── README.md                      # Project documentation
└── LICENSE                        # Licensing information
```

## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Install Dependencies**
   Navigate to the `src/lambda_function` directory and install the required Python packages if you want to test it locally on virtual environemtn:
   ```
   cd src/lambda_function
   pip install -r requirements.txt
   ```

3. **Deploy the Infrastructure**
   Use the pipeline-template.yaml in the `infra` directory to deploy the CI/CD pipeline.

4. **Trigger the Pipeline**
   Make changes to the Lambda function code and push to the repository to trigger the CodePipeline automatically.

## Usage

Once deployed, the Lambda function can be invoked through AWS services or directly via the AWS Management Console. The CI/CD pipeline will automatically build and deploy changes made to the Lambda function.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.