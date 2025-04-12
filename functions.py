import pyautogui
import platform
import psutil
import os
from datetime import datetime
from PIL import ImageGrab
from screeninfo import get_monitors

#⁡⁣⁣⁢СКРИНШОТЫ⁡
# ⁡⁢⁣⁡⁢⁣⁢Получает информацию о всех доступных мониторах⁡
def get_monitors_info():
    monitors = list(get_monitors())
    monitors_info = []
    
    for i, monitor in enumerate(monitors):
        monitor_info = {
            'id': i + 1,
            'width': monitor.width,
            'height': monitor.height,
            'x': monitor.x,
            'y': monitor.y,
            'monitor': monitor
        }
        monitors_info.append(monitor_info)
    
    return monitors_info

# ⁡⁢⁣⁡⁢⁣⁢Создает скриншот указанного монитора⁡
def take_screenshot(monitor_info):

    screenshot = ImageGrab.grab(bbox=(
        monitor_info['x'], monitor_info['y'],
        monitor_info['x'] + monitor_info['width'],
        monitor_info['y'] + monitor_info['height']
    ))
    return screenshot

# ⁡⁢⁣⁢Создает скриншоты всех указанных мониторов⁡
def take_screenshots_of_monitors(monitors_info):
    screenshots = []
    
    for monitor in monitors_info:
        screenshot = take_screenshot(monitor)
        screenshots.append(screenshot)
        
    return screenshots

#⁡⁣⁣⁢СИСТЕМА⁡
#⁡⁢⁣⁡⁢⁣⁢Получает информацию о операционной системе 
def get_system_info():
    system_info = {
        'os': platform.system(),
        'os_version': platform.version(),
        'os_release': platform.release(),
        'os_architecture': platform.machine(),
        'os_architecture': platform.architecture(),
        'os_architecture': platform.architecture(),
        'os_architecture': platform.architecture(),
    }   
    return system_info

#⁡⁢⁣⁡⁢⁣⁡⁢⁣⁢Получает информацию о процессоре⁡
def get_cpu_info():
    cpu_info = {
        'cpu_name': platform.processor(),
        'cpu_cores': psutil.cpu_count(logical=False),
        'cpu_frequency': psutil.cpu_freq()
        ,
        'cpu_usage': psutil.cpu_percent(interval=0.1),
        'cpu_usage_per_core': psutil.cpu_percent(interval=0.1, percpu=True)
    }
    return cpu_info 

print(get_cpu_info())