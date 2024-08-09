from .modules import ChatHandler, ChatListHandler


def setup(api):
    api.add_resource(ChatListHandler, '/chats')
    api.add_resource(ChatHandler, '/chats/<string:id>')
    return
