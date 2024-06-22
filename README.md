# End-to-End AI Customer Support Chatbot with deployment Flow

This project is an AI-powered customer support chatbot using Azure and OpenAI services. The chatbot can handle common customer queries and provide relevant information. 

- I have implemented this AI application using the End-to-End deployment Flow. 
- The main aim of this project is to show the deployment flow in a real world industry setting using all the tools and services for effective source control and deployments.

![openai-end-to-end-deployment-flow](image.png)

## Table of Contents

- [Customer Support Chatbot](#customer-support-chatbot)
  - [Table of Contents](#table-of-contents)
  - [Setup and Installation](#setup-and-installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a `.env` File](#2-create-a-env-file)
    - [3. Build and Run the Docker Container](#3-build-and-run-the-docker-container)
    - [4. Open in VS Code Dev Container](#4-open-in-vs-code-dev-container)
    - [5. Run the Application](#5-run-the-application)
    - [6. Run Tests](#6-run-tests)
    - [7. Check Code Standards](#7-check-code-standards)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [Development Environment](#development-environment)
    - [Dockerfile](#dockerfile)
    - [Docker Compose](#docker-compose)
    - [Dev Container Configuration](#dev-container-configuration)
  - [Contributing](#contributing)
  - [License](#license)


## Project Structure
```
customer-support-chatbot/
├── .devcontainer/
│   └── devcontainer.json
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── dev.yml
│       ├── test.yml
│       └── prod.yml
├── data/
│   └── sample_data.txt
├── src/
│   └── chatbot.py
├── tests/
│   ├── bulk_test_chatbot.py
│   └── test_chatbot.py
├── .env
├── .env.dev
├── .env.test
├── .env.prod
├── Dockerfile
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.test.yml
├── docker-compose.prod.yml
├── requirements.txt
├── README.md
└── .gitignore

```


## Prerequisites

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- OpenAI API key (sign up [here](https://www.openai.com/))

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AjayKrishna76/customer-support-chatbot.git
cd customer-support-chatbot
```

### 2. Create a `.env` File
Create a `.env` file in the root directory with the following content:
```bash
OPENAI_API_KEY=your_openai_api_key
```

### 3. Build and Run the Docker Container
Ensure Docker is installed on your system. Then run the following commands:
```bash
docker-compose up --build
```

### 4. Open in VS Code Dev Container
1. Open Visual Studio Code.
2. Use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and select `Remote-Containers: Open Folder in Container...`.
3. Select your project folder.

### 5. Run the Application
Inside the VS Code terminal, run:
```bash
python src/chatbot.py
```

### 6. Run Tests
Run the tests using pytest:
```bash
pytest
```

### 7. Check Code Standards
Check code standards using flake8:
```bash
flake8 src tests
```

## CI/CD Pipeline
The CI/CD pipeline is configured using GitHub Actions. It includes the following steps:

- Checkout code
- Set up Python
- Install dependencies
- Check code standards using flake8
- Run unit tests using pytest
- Run bulk tests
- Generate and upload coverage reports

## Environments

### Development Environment

The development environment is set up to allow developers to write and debug code. Use the following command to start the development environment locally:

```bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

## Test Environment
The test environment is used to run automated tests to validate changes. Use the following commands to deploy and run tests in the test environment locally:
```bash
docker-compose -f docker-compose.yml -f docker-compose.test.yml up --build -d
docker-compose -f docker-compose.yml -f docker-compose.test.yml run app
```
## Production Environment
The production environment is where the final version of the application runs for end-users. Deployment to production is handled by the CI/CD pipeline and triggered by tagging a release:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin --tags
```

### Dockerfile
```bash
FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "src/chatbot.py"]
```

### Docker Compose
```bash
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/usr/src/app
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
```

### Dev Container Configuration
```bash
{
  "name": "Python Development Container",
  "dockerFile": "Dockerfile",
  "context": "..",
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "extensions": [
    "ms-python.python",
    "ms-azuretools.vscode-docker"
  ],
  "postCreateCommand": "pip install -r requirements.txt",
  "remoteUser": "root",
  "runArgs": ["--env-file", ".env"]
}
```

## Test Environment Setup

The test environment is set up to ensure that the application is thoroughly tested in an isolated and controlled environment before deployment to production. This includes running automated tests, generating coverage reports, and validating the code quality.

### Test-Specific Environment Variables

A separate `.env.test` file is used to define environment variables specific to the test environment. This file is placed in the root directory of the project.

**Example `.env.test` file:**

```env
OPENAI_API_KEY=test_openai_api_key
```

## CI/CD Pipeline
The CI/CD pipeline is configured to handle different environments:

- Development: Triggered on push to the dev branch.
- Test: Triggered on pull request to the main branch.
- Production: Triggered on push of a version tag.



### Contributing
Contributions are welcome! Please open an issue or submit a pull request.
