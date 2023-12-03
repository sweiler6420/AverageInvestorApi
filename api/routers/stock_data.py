from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from .. import models, schemas, utils, oauth2
from ..database import get_db
from uuid import UUID

router = APIRouter(
    prefix="/v1/stock_data",
    tags=['Stock_data']
)

@router.get('', response_model=List[schemas.StockData])
def get_stock_data(db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user), limit: int = 108, offset: int = 0, search: Optional[str] = ""):
    stock_data = db.query(models.StockData.stock_id, (models.StockData.date + models.StockData.time).label("datetime"), models.StockData.open_price, models.StockData.high_price, models.StockData.low_price, models.StockData.close_price, models.StockData.volume) \
        .join(models.Stocks, models.StockData.stock_id == models.Stocks.stock_id, isouter=False).filter(models.Stocks.ticker_symbol.contains(func.lower(search))).order_by(models.StockData.date.asc(), models.StockData.time.asc()).limit(limit).offset(offset).all()

    if not stock_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Stock with id: {search} does not exist")

    return stock_data