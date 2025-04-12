import asyncio
import websockets
import json
from functions import take_screenshot, get_system_info, get_cpu_info, get_memory_info

async def connect_to_server():
    uri = "ws://localhost:8000/ws"  # Измените URI в соответствии с вашим сервером
    
    async with websockets.connect(uri) as websocket:
        print("Подключено к серверу")
        
        while True:
            try:
                # Получаем команду от сервера
                command = await websocket.recv()
                command = json.loads(command)
                
                # Обрабатываем различные команды
                if command["type"] == "get_system_info":
                    response = get_system_info()
                    await websocket.send(json.dumps(response))
                    
                elif command["type"] == "get_cpu_info":
                    response = get_cpu_info()
                    await websocket.send(json.dumps(response))
                    
                elif command["type"] == "get_memory_info":
                    response = get_memory_info()
                    await websocket.send(json.dumps(response))
                    
                elif command["type"] == "take_screenshot":
                    screenshot = take_screenshot(command["monitor_info"])
                    # Конвертируем скриншот в формат для отправки
                    screenshot_bytes = screenshot.tobytes()
                    await websocket.send(screenshot_bytes)
                    
            except websockets.exceptions.ConnectionClosed:
                print("Соединение с сервером разорвано")
                break
            except Exception as e:
                print(f"Ошибка: {str(e)}")
                continue

# Запускаем клиент
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())
