# 🚀 Serverless Calculator App 🧮

This is a serverless application for performing basic mathematical operations using AWS Lambda Functions.

## 📝 Table of Contents
1. [📖 Description](#-description)
2. [📂 Folder Structure](#-folder-structure)
3. [🛠️ Prerequisites](#️-prerequisites)
4. [🚀 How to Run](#️-how-to-run)
5. [🔍 Testing](#-testing)
6. [🚀 Deployment](#-deployment)
7. [🤝 Contributing](#-contributing)

## 📖 Description

The Serverless Calculator App consists of a Lambda function written in Python that performs addition, subtraction, multiplication, and division. It is deployed using AWS Lambda and can be triggered via API Gateway.

## 📂 Folder Structure

```
serverless-calculator-app/
│
├── lambda_function.py          # Lambda function code
├── test_lambda_function.py     # Test script for Lambda function
├── requirements.txt            # File specifying external dependencies
├── azure-pipeline.yml          # Azure DevOps pipeline configuration
└── .gitignore                  # File specifying which files to ignore in Git
```

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed locally.
- An AWS account with permissions to create and manage Lambda functions.
- Azure DevOps account for setting up the deployment pipeline.

## 🚀 How to Run

To run the Serverless Calculator App locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/serverless-calculator-app.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Lambda function locally (for testing purposes):

   ```bash
   # Example command:
   python lambda_function.py
   ```

## 🔍 Testing

To test the Lambda function, run the test script:

```bash
python test_lambda_function.py
```

## 🚀 Deployment

The deployment of the Serverless Calculator App is automated using Azure DevOps pipeline. Configure the pipeline with your AWS credentials and necessary configurations.

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.
