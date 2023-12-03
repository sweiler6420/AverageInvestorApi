from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import user, auth, stock, stock_data, watchlist

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(stock.router)
app.include_router(stock_data.router)
app.include_router(watchlist.router)

#Just for testing
@app.get("/")
def root():
    return {"message": "Hello World"}

