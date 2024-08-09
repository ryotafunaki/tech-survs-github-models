from dataclasses import dataclass


@dataclass
class ChatCreateRequest:
    message: str


@dataclass
class ChatCreateResponse:
    id: str


@dataclass
class ChatGetResponse:
    message: str
