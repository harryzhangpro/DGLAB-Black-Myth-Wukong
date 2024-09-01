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
        async with websockets.connect(uri) as websocket:
            await websocket.send(json_message)
            print(f"Sent: {json_message}")
            
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=0.10)  # 设置接收超时
                print(f"Received: {response}")
            except asyncio.TimeoutError:
                print("Error: Timed out waiting for a response from the server.")
            
    except asyncio.TimeoutError:
        print("Error: Connection timed out while trying to send the message.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Error: Connection closed with error: {e}")
    except Exception as e:
        print(f"Error: Failed to send message due to: {e}")

