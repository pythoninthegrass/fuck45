#!/usr/bin/env python

from eliot import log_call, to_file
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import articles, submissions

to_file(sys.stdout)
# to_file(open("/tmp/get_secrets.log", "w"))

app = FastAPI()

# Mount the static files
app.mount("/static", StaticFiles(directory="frontend/public"), name="static")

# Include your routers
app.include_router(articles.router)
app.include_router(submissions.router)
