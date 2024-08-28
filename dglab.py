import websockets
import json

async def send_message():
    # 连接到WebSocket服务器
    uri = "ws://192.168.31.61:60536/1" # IP地址改这里
    async with websockets.connect(uri) as websocket:
        # 要发送的数据
        message = {
            "cmd": "set_pattern",
            "pattern_name": "经典",
            "intensity": 100,
            "ticks": 30
        }
        
        # 将Python字典转换为JSON字符串
        json_message = json.dumps(message)
        
        # 发送JSON消息
        await websocket.send(json_message)
        print(f"Sent: {json_message}")
