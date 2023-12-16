from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from .. import models, schemas, utils, oauth2
from ..database import get_db
from uuid import UUID
from typing import List
import math

router = APIRouter(
    prefix="/v1/watchlist",
    tags=['Watchlist']
)


@router.get("/{watchlist_id}", response_model=List[schemas.Stocks])
def get_watchlist(watchlist_id: UUID, db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)):
    
    watchlist = db.query(models.Watchlist).filter(models.Watchlist.watchlist_id == watchlist_id, models.Watchlist.user_id == current_user.user_id).first()
    if not watchlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Watchist does not exist")

    watchlist_data = db.query(models.WatchlistData.stock_id, models.Stocks.ticker_symbol, models.Stocks.company, models.Stocks.market, models.Stocks.isin).join(models.Stocks, models.WatchlistData.stock_id == models.Stocks.stock_id) \
        .filter(models.WatchlistData.watchlist_id == watchlist_id).order_by(models.WatchlistData.position.asc()).all()
    
    if not watchlist_data:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail="No Stocks in this Watchlist")

    return watchlist_data

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateWatchlist)
def create_watchlist(title: str = "", db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)):
    watchlist = {
        'user_id': current_user.user_id
    }
    
    if title:
        watchlist['title'] = title

    new_watchlist = models.Watchlist(**watchlist)
    db.add(new_watchlist)
    db.commit()
    db.refresh(new_watchlist)

    return new_watchlist

@router.post("/stock", status_code=status.HTTP_201_CREATED, response_model=schemas.WatchlistData)
def add_watchlist_stock(stock_id: UUID, watchlist_id: UUID, db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)):
    stock_exists = db.query(models.WatchlistData).filter(models.WatchlistData.watchlist_id == watchlist_id, models.WatchlistData.stock_id == stock_id).first()
    if stock_exists:   
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Stock: {stock_id} Already Exists")

    watchlist = db.query(models.WatchlistData).filter(models.WatchlistData.watchlist_id == watchlist_id).order_by(models.WatchlistData.position.asc()).all()
    for i in range(len(watchlist)):
        watchlist[i].position = watchlist[i].position + 1
    
    watchlist = {
        'watchlist_id': watchlist_id,
        'stock_id': stock_id,
        'position': 0
    }

    new_watchlist_stock = models.WatchlistData(**watchlist)
    db.add(new_watchlist_stock)
    db.commit()
    db.refresh(new_watchlist_stock)

    return new_watchlist_stock

@router.put("/stock", status_code=status.HTTP_201_CREATED, response_model=List[schemas.Stocks])
def reposition_stock(stock_id: UUID, destination_index: int, current_index: int, watchlist_id: UUID, db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)):
   
    watchlist = db.query(models.WatchlistData).filter(models.WatchlistData.watchlist_id == watchlist_id).order_by(models.WatchlistData.position.asc()).all()

    if current_index > destination_index:
        watchlist[current_index].position = destination_index

        for i in range(len(watchlist)):
            if i >= destination_index and i < current_index:
                watchlist[i].position = watchlist[i].position + 1

    if current_index < destination_index:
        watchlist[current_index].position = destination_index

        for i in range(len(watchlist)):
            if i <= destination_index and i > current_index:
                watchlist[i].position = watchlist[i].position - 1

    db.commit()
    
    watchlist_data = db.query(models.WatchlistData.stock_id, models.Stocks.ticker_symbol, models.Stocks.company, models.Stocks.market, models.Stocks.isin).join(models.Stocks, models.WatchlistData.stock_id == models.Stocks.stock_id) \
        .filter(models.WatchlistData.watchlist_id == watchlist_id).order_by(models.WatchlistData.position.asc()).all()

    return watchlist_data