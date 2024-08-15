# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from .chat_handler import ChatHandler
from .chat_list_handler import ChatListHandler


def setup(api):
    api.add_resource(ChatListHandler, '/chats')
    api.add_resource(ChatHandler, '/chats/<string:id>')
    return
