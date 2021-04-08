from pydantic import BaseModel


class Chat(BaseModel):
    id: int


class Message(BaseModel):
    message_id: int

    chat: Chat
    date: int
    text: str


class Update(BaseModel):
    update_id: int
    message: Message


class MessageReply(BaseModel):
    chat_id: int
    text: str