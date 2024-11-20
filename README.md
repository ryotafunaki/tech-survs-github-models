# GitHub Models Technical Survey Project Repository

This repository is a technical survey of the GitHub Models.

## Overview

## Requirements

- Python 3.12 and above

### Execution on local machine

1.  Set the environment variables
    | Name       | Description                             | Value |
    | ---------- | --------------------------------------- | ----- |
    | CHAT_DB_FILE | Chat database file path | *File path* |
    | AZURE_AI_ENDPOINT | Azure AI endpoint | https://models.inference.ai.azure.com |
    | GITHUB_TOKEN | GitHub token | *Your GitHub token* |

    e.g.
    ```bash
    export CHAT_DB_FILE=./chat.db
    export AZURE_AI_ENDPOINT=https://models.inference.ai.azure.com
    export GITHUB_TOKEN=<Your GitHub token>
    ``` 

1.  Start the application
    ```bash
    poetry run python main.py
    ```

1.  Request the application
    ```bash
    curl -X 'POST' \
    'http://localhost:5000/chats' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "message": "Hello, World!"
    }'
    ```

1.  Get a response from your application
    ```bash
    curl http://localhost:5000/chats/1
    ```

> [!NOTE]  
> Check chat requests at 5-second intervals.
