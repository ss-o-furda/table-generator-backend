from fastapi import FastAPI
from .models import db


def get_app():
    app = FastAPI(title="Table Generator Backend")
    db.init_app(app)
    return app
