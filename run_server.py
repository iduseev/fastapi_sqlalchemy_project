#!/usr/bin/env python3
import uvicorn

from backend.app import app


# driver code
if __name__ == "__main__":
    uvicorn.run("run_server:app", host="127.0.0.1", port=8080, reload=True)
