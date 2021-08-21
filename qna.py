# Imports
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Response
from typing import Dict, List
import asyncio


class Room:
    def __init__(self):
        self.sockets: List[WebSocket] = []

    async def add_socket(self, socket: WebSocket):
        if socket not in self.sockets:
            self.sockets.append(socket)

    async def remove_socket(self, socket: WebSocket):
        if socket in self.sockets:
            await socket.close()
            self.sockets.remove(socket)

    async def remove_sockets(self):
        remove_queue = []

        for socket in self.sockets:
            remove_queue.append(socket.close())

        if len(remove_queue) != 0:
            await asyncio.wait(remove_queue)

        self.sockets.clear()

    async def broadcast(self, message: str, sender: WebSocket):
        send_queue = []

        for socket in self.sockets:
            if socket != sender:
                send_queue.append(socket.send_text(message))

        if len(send_queue) != 0:
            await asyncio.wait(send_queue)


# FastAPI setup
qna = FastAPI()

rooms: Dict[str, Dict[str, Room]] = {}


# Health Check
@qna.get("/healthcheck")
async def handle_healthcheck():
    return Response()


# Message relaying
@qna.websocket("/ws/{cohort}/{code}")
async def handle_socket(websocket: WebSocket, cohort: str, code: str):
    if cohort not in rooms.keys():
        print(f"Creating cohort \"{cohort}\".")
        rooms[cohort] = {}

    if code not in rooms[cohort].keys():
        print(f"Opening room \"{code}\".")
        rooms[cohort][code] = Room()

    await websocket.accept()
    await rooms[cohort][code].add_socket(websocket)

    while True:
        try:
            message = await websocket.receive_text()
            await rooms[cohort][code].broadcast(message, websocket)

        except WebSocketDisconnect:
            print(
                f"Socket disconnected from room \"{code}\", {len(rooms[cohort][code].sockets) - 1} sockets remaining.")

            await rooms[cohort][code].remove_socket(websocket)
            if len(rooms[cohort][code].sockets) == 0:
                print(f"Closing room \"{code}\".")
                await rooms[cohort][code].remove_sockets()
                del rooms[cohort][code]
                if len(rooms[cohort].keys()) == 0:
                    print(f"Destroying cohort \"{cohort}\".")
                    del rooms[cohort]
            break

        except Exception as err:
            print(f"Unexpected error in room \"{code}\", closing room.")
            print(err)

            try:
                del rooms[cohort][code]
                if len(rooms[cohort].keys()) == 0:
                    print(f"Destroying cohort \"{cohort}\".")
                    del rooms[cohort]
            except:
                pass
            break


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("qna:qna", host="0.0.0.0", port=4000, log_level="info")
