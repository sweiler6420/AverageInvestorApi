from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIME, DATE, TIMESTAMP, NUMERIC, VARCHAR, BIGINT, INTEGER
from enum import Enum
from .database import Base

class User(Base):
    __tablename__ = "users"
    # __table_args__ =  {'schema' : 'avg_inv'}

    user_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=text('gen_random_uuid()'))
    username = Column(String, nullable = False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Stocks(Base):
    __tablename__ = "stocks"

    stock_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=text('gen_random_uuid()'))
    ticker_symbol = Column(VARCHAR(length=5), nullable = False, unique=True)
    company = Column(VARCHAR(length=150), nullable=False, unique=True)
    market = Column(VARCHAR(length=150), nullable=False)
    isin = Column(VARCHAR(length=12), nullable=False)

class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(BIGINT, server_default = text("nextval('avg_inv.stock_data_seq'::regclass)"), primary_key=True)
    stock_id = Column(UUID(as_uuid=True), ForeignKey("avg_inv.stocks.stock_id"), nullable=False)
    date = Column(DATE, nullable = False)
    time = Column(TIME, nullable=False)
    open_price = Column(NUMERIC(precision=8,scale=2), nullable=False)
    high_price = Column(NUMERIC(precision=8,scale=2), nullable=False)
    low_price = Column(NUMERIC(precision=8,scale=2), nullable=False)
    close_price = Column(NUMERIC(precision=8,scale=2), nullable=False)
    volume = Column(BIGINT, nullable=False)

    owner = relationship("Stocks")

class Watchlist(Base):
    __tablename__ = "watchlists"

    watchlist_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=text('gen_random_uuid()'))
    title = Column(VARCHAR(length=50), nullable=False, server_default='My Watchlist')
    user_id = Column(UUID(as_uuid=True), ForeignKey("avg_inv.users.user_id"), nullable=False)

class WatchlistData(Base):
    __tablename__ = "watchlist_data"
    
    watchlist_id = Column(UUID(as_uuid=True), ForeignKey("avg_inv.watchlists.watchlist_id"), nullable=False)
    stock_id = Column(UUID(as_uuid=True), ForeignKey("avg_inv.stocks.stock_id"), nullable=False)
    position = Column(INTEGER, nullable=False)

    __mapper_args__ = { 
        "primary_key": [watchlist_id, stock_id]
    }

class Politician(Base):
    __tablename__ = "politicians"

    politician_id = Column(VARCHAR(length=50), primary_key=True, nullable=False)
    state = Column(VARCHAR(length=5), nullable=True)
    chamber = Column(VARCHAR(length=50), nullable=True)
    dob = Column(DATE, nullable=True)
    first_name = Column(VARCHAR(length=80), nullable=False)
    last_name = Column(VARCHAR(length=80), nullable=False)
    gender = Column(VARCHAR(length=25), nullable=True)
    party = Column(VARCHAR(length=50), nullable=False)