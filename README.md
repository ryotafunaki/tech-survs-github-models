# Python Project Repository

This repository is a Python Project.

## Overview

## Requirements

- Python 3.12 and above

## Container image info

## How to use

### Execution on local machine

1.  Set the environment variables
    | Name       | Description                             | Value |
    | ---------- | --------------------------------------- | ----- |
    | AZURE_AI_ENDPOINT |   | https://models.inference.ai.azure.com |
    | GITHUB_TOKEN | The port number of the cache server     | *Your GitHub Token*  |
    e.g.
    ```bash
    export AZURE_AI_ENDPOINT=https://models.inference.ai.azure.com
    export GITHUB_TOKEN=<Your GitHub Token>
    ``` 

1.  Start the application
    ```bash
    poetry run python main.py
    ```

1. Request the application
    ```bash
    curl -X POST http://localhost:5000/chats -d '{"message": "Hello, World!"}'
    curl http://localhost:5000/chats/1
    ```
