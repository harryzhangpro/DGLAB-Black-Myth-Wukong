import websockets
import json
import asyncio

async def send_message():
    uri = "ws://192.168.31.61:60536/1"  # IP地址改这里
    message = { 
        "cmd": "set_pattern",  
        "A_pattern_name": "经典",  
        "A_intensity": 100, 
        "A_ticks": 30  
    }
    
    # 将Python字典转换为JSON字符串
    json_message = json.dumps(message)
    
    try:
        async with websockets.connect(uri, ping_interval=None) as websocket:
            send_task = asyncio.create_task(asyncio.wait_for(websocket.send(json_message), timeout=0.25))
            
            print(f"Sent: {json_message}")
    except asyncio.TimeoutError:
        print("Error: Connection timed out while trying to send the message.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Error: Connection closed with error: {e}")
    except Exception as e:
        print(f"Error: Failed to send message due to: {e}")
