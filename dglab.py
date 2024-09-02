import websockets
import json
import asyncio

async def send_message(intensity, ticks):
    uri = "ws://192.168.31.61:60536/1"  # IP地址改这里
    message = {  
        "cmd": "set_pattern",  
        "pattern_name": "经典",  
        "intensity": intensity,  
        "ticks": ticks  
    }
    
    json_message = json.dumps(message)
    
    try:
        # 使用 asyncio.wait_for 包装连接操作，以设置连接超时
        websocket = await asyncio.wait_for(websockets.connect(uri), timeout=0.10)
        async with websocket:
            try:
                await asyncio.wait_for(websocket.send(json_message), timeout=0.10)  # 设置发送超时
                print(f"Sent: {json_message}")
            except asyncio.TimeoutError:
                print("Error: Timed out waiting for a response from the server.")
            
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=0.10)  # 设置接收超时
                print(f"Received: {response}")
            except asyncio.TimeoutError:
                print("Error: Timed out waiting for a response from the server.")
            
    except asyncio.TimeoutError:
        print("Error: Connection timed out while trying to connect to the server.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Error: Connection closed with error: {e}")
    except Exception as e:
        print(f"Error: Failed to send message due to: {e}")

