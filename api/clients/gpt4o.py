# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import json
import os
from dataclasses import dataclass

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential


@dataclass
class Gpt4oConfig:
    system_messages: list[str]
    temperature: float
    max_tokens: int
    top_p: float


@dataclass
class Config:
    endpoint: str
    credential: AzureKeyCredential
    gpt4o_config: Gpt4oConfig


def get_credential():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return None
    credential = AzureKeyCredential(token)
    return credential


def load_gpu4o_config():
    with open("gpt4o.config.json") as f:
        json_data = json.load(f)
        config = Gpt4oConfig(
            system_messages=" ".join(
                json_data["systemMessages"]) if "systemMessages" in json_data else "",
            temperature=json_data["temperature"],
            max_tokens=json_data["maxTokens"],
            top_p=json_data["topP"]
        )
    return config


config = Config(
    endpoint=os.getenv("AZURE_AI_ENDPOINT"),
    credential=get_credential(),
    gpt4o_config=load_gpu4o_config()
)


class Gpt4oClient:
    def __init__(self):
        pass

    def setup(self) -> None:
        self.__client = ChatCompletionsClient(
            endpoint=config.endpoint,
            credential=config.credential
        )
        self.__system_message = config.gpt4o_config.system_messages
        return

    def complete(self, messages: str) -> str:
        conf = config.gpt4o_config
        response = self.__client.complete(
            messages=[
                SystemMessage(content=self.__system_message),
                UserMessage(content=messages),
            ],
            model="gpt-4o-mini",
            temperature=conf.temperature,
            max_tokens=conf.max_tokens,
            top_p=conf.top_p
        )
        message = response.choices[0].message.content
        return message
