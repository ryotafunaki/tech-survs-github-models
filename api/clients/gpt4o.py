
import json
import os
from dataclasses import dataclass

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential


@dataclass
class Gpt4oConfig:
    temperature: float
    max_tokens: int
    top_p: float

    def __init__(self, **entries):
        self.__dict__.update(entries)
        return


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
        config = Gpt4oConfig(**json_data)
    return config


config = Config(
    endpoint=os.getenv("AZURE_AI_ENDPOINT"),
    credential=get_credential(),
    gpt4o_config=load_gpu4o_config()
)


class Gpt4oClient:
    def __init__(self):
        pass

    def setup(self, system_message: str) -> None:
        self.__client = ChatCompletionsClient(
            endpoint=config.endpoint,
            credential=config.credential
        )
        self.__system_message = system_message
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
