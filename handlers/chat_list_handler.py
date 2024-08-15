# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from dataclasses import asdict
from http import HTTPStatus

from flask import request
from flask_restful import Resource, abort

from api.clients import SqliteClient
from models import ChatCreateRequest, ChatCreateResponse


class ChatListHandler(Resource):
    def post(self):
        body = request.get_json()
        if not body:
            abort(HTTPStatus.NOT_FOUND.value)
        try:
            req_body = ChatCreateRequest(**body)
            message = req_body.message
        except TypeError:
            abort(HTTPStatus.NOT_FOUND.value)

        db_client = SqliteClient()
        created = db_client.create_table()
        if not created:
            abort(HTTPStatus.SERVICE_UNAVAILABLE.value)
        id = db_client.insert_message(message)
        response = ChatCreateResponse(id)
        return asdict(response), HTTPStatus.CREATED.value
