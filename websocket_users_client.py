import asyncio
import websockets

#Установка соединения
async def client():
    uri = "ws://localhost:8765"
    #Отправка сообщения
    async with websockets.connect(uri) as websocket:
        message = f'Привет, сервер!'
        await websocket.send(message)
        #Получение ответа и вывод в консоль
        for i in range(5):
            response = await websocket.recv()
            print(response)

asyncio.run(client())