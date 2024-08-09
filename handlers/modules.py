# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from dataclasses import asdict

from flask_restful import Resource

from api.clients import Gpt4oClient
from models import ChatCreateResponse, ChatGetResponse


class ChatListHandler(Resource):
    def post(self):
        response = ChatCreateResponse(1)
        return asdict(response)


class ChatHandler(Resource):
    def get(self, id):
        client = Gpt4oClient()
        client.setup(
            """You are a cheerful cat, and the words suffix is "nya". You speak in Japanese.""")
        message = client.complete("おはよう")
        response = ChatGetResponse(message=message)
        return asdict(response)
