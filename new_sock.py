import asyncio
import websockets
import pyautogui

# Define the WebSocket handler
async def handler(websocket):
    while True:
        msg = await websocket.recv()
        print(msg)
        if msg == "w":
            pyautogui.press("w")
        elif msg == "a":
            pyautogui.press("a")
        elif msg == "s":
            pyautogui.press("s")
        elif msg == "d":
            pyautogui.press("d")

# Main function to start the WebSocket server
async def main():
    # Start the WebSocket server
    async with websockets.serve(handler, "192.168.31.87", 8000):
        print("WebSocket server started on ws://localhost:8000")
        await asyncio.Future()  # Run forever


# Run the server
if __name__ == "__main__":
    asyncio.run(main())
