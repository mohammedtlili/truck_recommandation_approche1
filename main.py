from fastapi import FastAPI
from uvicorn import Server, Config
from fastapi.middleware.cors import CORSMiddleware

from configuration.config import  ServerSettings
import controllers.routes


host = ServerSettings.SERVER_HOST
port = ServerSettings.SERVER_PORT

app = FastAPI(title="Tarification_App")
app.include_router(controllers.routes.router)

# Creating origins for CORS and angular requests
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == '__main__':
    server = Server(Config(app=app, host=host, port=port))
    server.run()
