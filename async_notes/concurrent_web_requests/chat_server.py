import asyncio
import logging


class ChatServer:
    def __init__(self):
        self._usernames = {}

    async def start_chat_server(self, host: str, port: int) -> None:
        server = await asyncio.start_server(self.client_connected, host, port)

        async with server:
            print("starting chat server")
            await server.serve_forever()

    async def client_connected(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        command = await reader.readline()
        command, args = command.split(b' ')
        if command == b'CONNECT':
            username = args.decode().strip()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)
        else:
            logging.error(f" Got invalid command: {command}, disconnection")
            writer.close()
            await writer.wait_closed()

    def _add_user(self, username: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        self._usernames[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _listen_for_messages(self, username: str, reader: asyncio.StreamReader) -> None:
        try:
            while (data := await asyncio.wait_for(reader.readline(), 600)) != b'':
                await self._notify_all(username, f"{data.decode()}")
        except Exception as e:
            logging.exception(f"Error reading from client", exc_info=e)
            await self._remove_user(username)
            await self._notify_all(username, f"has left the chat.\n")

    async def _on_connect(self, username: str, writer: asyncio.StreamWriter):
        writer.write(f"Welcome{username}! {len(self._usernames)} users are online!\n".encode())
        await writer.drain()
        await self._notify_all(username, f"has joined the chat")

    async def _notify_all(self, username: str, message: str) -> None:
        inactive_users = []
        for username, writer in self._usernames.items():
            if username == username:
                continue
            try:
                writer.write(f'{username}: {message}'.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception('Could not write to client.', exc_info=e)
                inactive_users.append(username)

        [await self._remove_user(username) for username in inactive_users]

    async def _remove_user(self, username: str):
        writer = self._usernames[username]
        del self._usernames[username]

        try:
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            logging.exception('Could not close connection.', exc_info=e)


async def main() -> None:
    server = ChatServer()
    await server.start_chat_server('localhost', 8086)


asyncio.run(main())
