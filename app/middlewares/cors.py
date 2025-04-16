from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("uvicorn.error")

def setup_cors(app: FastAPI):
    """
    Configure CORS restrictively.
    Adjust the list of allowed origins based on your environment (development/production).
    """
    origins = [
        "*"
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,            # "*" is not used in production
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["Authorization", "Content-Type"],
    )

def setup_global_exception_handler(app: FastAPI):
    """
    Configure a global middleware to capture and log exceptions.
    This prevents internal errors from spreading uncontrollably and hides sensitive details.
    """
    @app.middleware("http")
    async def global_exception_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            logger.error(f"Request error {request.url}: {exc}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={"detail": "An internal server error occurred."},
            )