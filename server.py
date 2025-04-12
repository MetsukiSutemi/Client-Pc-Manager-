from fastapi import FastAPI, WebSocket
import json

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Клиент подключен")
    
    try:
        while True:
            # Отправляем команды клиенту
            commands = [
                {"type": "get_system_info"},
                {"type": "get_cpu_info"}, 
                {"type": "get_memory_info"},
                {"type": "take_screenshot", "monitor_info": {"width": 1920,"height": 1080,"x": 0,"y": 0}}
            ]
            
            for command in commands:
                await websocket.send_json(command)
                
                # Получаем ответ от клиента
                if command["type"] == "take_screenshot":
                    response = await websocket.receive_bytes()
                    # Сохраняем полученный скриншот в файл
                    from PIL import Image
                    import io
                    
                    # Преобразуем байты в изображение
                    screenshot = Image.frombytes('RGB', (1920, 1080), response)
                    
                    # Сохраняем изображение
                    screenshot.save('screenshot.png')
                    print("Скриншот сохранен")
                else:
                    response = await websocket.receive_json()
                print(f"Получен ответ")
                
    except Exception as e:
         print(f"Ошибка")
    # finally:
    #     print("Клиент отключен")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
