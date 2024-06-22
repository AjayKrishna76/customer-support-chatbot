# End-to-End AI Customer Support Chatbot with deployment Flow

This project is an AI-powered customer support chatbot using Azure and OpenAI services. The chatbot can handle common customer queries and provide relevant information. 

- I have implemented this AI application using the End-to-End deployment Flow. 
- The main aim of this project is to show the deployment flow in a real world industry setting using all the tools and services for effective source control and deployments.

![openai-end-to-end-deployment-flow](image.png)

## Project Structure
```
customer-support-chatbot/
│
├── .devcontainer/
│ └── devcontainer.json
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│ └── sample_data.txt
│
├── src/
│ └── chatbot.py
├── tests/
│ └── test_chatbot.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)
- OpenAI API key (sign up [here](https://www.openai.com/))

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AjayKrishna76/customer-support-chatbot.git
cd customer-support-chatbot
```

```bash
OPENAI_API_KEY=your_openai_api_key
```Testing CI pipeline
