from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from loguru import logger


async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        logger.error(
            f"HTTPException occurred: {exc.detail} - Status code: {exc.status_code} "
            f"while processing request {request.method} {request.url}"
        )
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": f"HTTP {exc.status_code} Error", "message": exc.detail},
        )
    else:
        logger.error(
            f"Unexpected exception occurred: {type(exc).__name__} - {str(exc)} "
            f"while processing request {request.method} {request.url}"
        )
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "message": str(exc)},
        )
