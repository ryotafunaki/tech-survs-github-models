# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import time

from api.clients.gpt4o import Gpt4oClient
from api.clients.sqlite import SqliteClient, Status


class MessageProcessor:
    @staticmethod
    def worker():
        while True:
            db_client = SqliteClient()
            created = db_client.create_table()
            time.sleep(5)
            if not created:
                continue
            message = db_client.get_next_message()
            if message is None:
                continue
            message.status = Status.PROCESSING
            db_client.update_message(message)

            llm_client = Gpt4oClient()
            llm_client.setup()
            response = llm_client.complete(message.message)

            message.status = Status.SUCCESS
            message.message = response
            db_client.update_message(message)
