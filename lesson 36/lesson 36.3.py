import asyncio

async def server_connection(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()

async def start_echo_server():
    server = await asyncio.start_server(
        server_connection, '127.0.0.1', 12345)

    addr = server.sockets[0].getsockname()
    print(f'Сервер запущений на {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(start_echo_server())
