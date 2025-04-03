# Secrets Manager

## Description
Command Line based password manager utilising AWS Secrets Manager to create, update, delete, list, download and create random passwords.


## Technologies used
- **Python:** Version 3.12
- **AWS:** Secrets Manager
- **Data Formats:** TXT for exporting password information from AWS locally
- **Automation Tools:**  CI/CD for deployment

## Installation

### Prerequisites
- [Python](https://www.python.org/downloads/) - version 3.12 or above
- [Make](https://www.gnu.org/software/make/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

### AWS requirements
- required secret keys:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ScrappyNozicka/Secrets-Manager
   cd totesys-final-project
2. Install dependencies:
    - `create-environment`(automated by `requirements`): Creates a Python virtual environment.
        ```bash
        make create-environment
    - `requirements`: Installs the project dependencies from requirements.txt.
        ```bash
        make requirements
    - `dev-setup`: Installs development tools(bandit, black, flake8, pytest-cov, and pip-audit)
        ```bash
        make dev-setup
    - `run-checks`: Runs security tests, code checks, unit tests, coverage analysis
        ```bash
        make run-checks
3. Set up AWS credentials:
    ```bash
    aws configure
