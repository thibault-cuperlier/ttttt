import asyncio
import websockets

connected = set()

async def handler(websocket, _):
    print("🔗 Client connecté")
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("❌ Déconnexion")
    finally:
        connected.remove(websocket)

async def main():
    print("🚀 Serveur WebSocket en écoute sur ws://0.0.0.0:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
