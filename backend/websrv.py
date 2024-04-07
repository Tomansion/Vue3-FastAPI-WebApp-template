from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from controller.notes import router as party_router
from utils.socket_utils import connection_manager
from pathlib import Path
from init import init

PORT = 3000

# Initialize the FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(party_router, prefix="/api")


# Add alive status route
@app.get("/api")
async def alive():
    return {"status": "alive"}


# Websocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast(f"Message text was: {data}")
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
        await connection_manager.broadcast("A client just disconnected.")


# Serve the Vue app in production mode
try:
    # Directory where Vue app build output is located
    build_dir = Path(__file__).resolve().parent / "dist"
    index_path = build_dir / "index.html"

    # Serve assets files from the build directory
    app.mount("/assets", StaticFiles(directory=build_dir / "assets"), name="assets")

    # Catch-all route for SPA
    @app.get("/{catchall:path}")
    async def serve_spa(catchall: str):
        # If the requested file exists, serve it, else serve index.html
        path = build_dir / catchall
        if path.is_file():
            return FileResponse(path)
        return FileResponse(index_path)

except RuntimeError:
    # The build directory does not exist
    print("No build directory found. Running in development mode.")


# Initialize the app
init()

print("\nRunning FastAPI app...")
print(" - FastAPI is available at " + f"http://localhost:{PORT}/api")
print(" - Swagger UI is available at " + f"http://localhost:{PORT}/docs")
print(" - Redoc is available at " + f"http://localhost:{PORT}/redoc")
print("")
