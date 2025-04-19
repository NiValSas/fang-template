from fastapi import FastAPI
from app.middlewares.cors import setup_cors, setup_global_exception_handler
import uvicorn

app = FastAPI()

def create_app() -> FastAPI:
    app = FastAPI()

    # Configure CORS
    setup_cors(app)
    setup_global_exception_handler(app)


    # Base route
    @app.get("/")
    def read_root():
        return {"message": "Fang project is running with automatic deploy by Innome 𓆉"}

    # Include routers
    # app.include_router()

    return app


# Global app instance
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)