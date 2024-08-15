# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import os
import sqlite3
from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class Config:
    filepath: str


config = Config(
    filepath=os.getenv("CHAT_DB_FILE"),
)


class Status(Enum):
    WAITING = ""
    PROCESSING = "P"
    SUCCESS = "S"
    FAILED = "F"


@dataclass
class Message:
    id: int
    status: str
    message: Optional[str]


class SqliteClient:
    def __init__(self):
        pass

    def create_table(self) -> bool:
        filepath = config.filepath
        with sqlite3.connect(filepath) as db:
            cursor = db.cursor()
            try:
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS message (id INTEGER PRIMARY KEY AUTOINCREMENT, status TEXT, message TEXT)')
                db.commit()
            except sqlite3.OperationalError:
                db.rollback()
                return False
        return True

    def insert_message(self, message: str) -> int:
        filepath = config.filepath
        with sqlite3.connect(filepath) as db:
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO message (status, message) VALUES (:status, :message)',
                {
                    "status": Status.WAITING.value,
                    "message": message
                })
            id = cursor.lastrowid
        return id

    def update_message(self, message: Message) -> bool:
        filepath = config.filepath
        with sqlite3.connect(filepath) as db:
            cursor = db.cursor()
            cursor.execute(
                'UPDATE message SET status = :status, message = :message WHERE id = :id',
                {
                    "status": message.status.value,
                    "message": message.message,
                    "id": message.id
                })
            db.commit()
        return True

    def get_message(self, id: int) -> Optional[str]:
        filepath = config.filepath
        with sqlite3.connect(filepath) as db:
            cursor = db.cursor()
            cursor.execute(
                'SELECT message FROM message WHERE id = :id',
                {
                    "id": id
                })
            message = cursor.fetchone()
        message = message[0] if message else None
        return message

    def get_next_message(self) -> Optional[Message]:
        filepath = config.filepath
        with sqlite3.connect(filepath) as db:
            cursor = db.cursor()
            cursor.execute(
                'SELECT id, message FROM message WHERE status = :status ORDER BY id ASC LIMIT 1',
                {
                    "status": Status.WAITING.value
                })
            row = cursor.fetchone()
        if not row:
            return None
        message = Message(
            id=row[0],
            status=Status.WAITING.value,
            message=row[1]
        )
        return message
