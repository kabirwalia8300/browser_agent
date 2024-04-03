import uvicorn

if __name__ == "__main__":
    uvicorn.run("fastapi_backend:app", host="0.0.0.0", port=8000)
