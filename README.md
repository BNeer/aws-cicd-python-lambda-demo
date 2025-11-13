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

3. **Connection to GitHub for Source stage in Pipeline**
1. Open your GitHub account.
2. In the top-right corner, click your profile picture → Settings → Developer settings.
3. Go to Personal access tokens → Tokens (classic) → Generate new token → Generate new token (classic).
4. Give the token a meaningful Note (e.g., codepipeline-github-token).
5. Set Expiration to No expiration (or if you wish to give an expiry date, select that one).
6. Under Select scopes, choose:
        repo
        admin:repo_hook
7. Click "Generate token"
8. Copy and save the generated token securely (you won’t be able to view it again).
9. In your AWS account, open AWS Secrets Manager → Store a new secret → Other type of secret.
10. Add a key named token, and paste the GitHub token as the value.
11. In the next window, under “Secret name”, provide a clear AWS-specific name such as     
    codepipeline-github-access-token, then click Next → Next → Store 

4. **Deploy the Infrastructure**
   Use the pipeline-template.yaml in the `infra` directory to deploy the CI/CD pipeline.

5. **Trigger the Pipeline**
   Make changes to the Lambda function code and push to the repository to trigger the CodePipeline automatically.

## Usage

Once deployed, the Lambda function can be invoked through AWS services or directly via the AWS Management Console. The CI/CD pipeline will automatically build and deploy changes made to the Lambda function.

