# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from dataclasses import asdict
from http import HTTPStatus

from flask_restful import Resource, abort

from api.clients import SqliteClient
from models import ChatGetResponse


class ChatHandler(Resource):
    def get(self, id):
        db_client = SqliteClient()
        created = db_client.create_table()
        if not created:
            abort(HTTPStatus.SERVICE_UNAVAILABLE.value)
        message = db_client.get_message(id)
        if not message:
            abort(HTTPStatus.NOT_FOUND.value)
        response = ChatGetResponse(message=message)
        return asdict(response), HTTPStatus.OK.value
