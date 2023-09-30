from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text
from .. import models, schemas, utils, oauth2
from ..database import get_db
from ..database import engine
from uuid import UUID

router = APIRouter(
    prefix="/v1/users",
    tags=['Users']
)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Possible raw sql statement for now...
    # user = db.query(models.User.__table__).from_statement(text("""select * from avg_inv.users where user_id=:user_id""")).params(user_id="5ed8597e-7aac-4f02-893f-f52e93eef7ec").all()
    # user2 = [dict(row) for row in user]
    # print(user2)

    test_user = db.query(models.User).filter(models.User.email == user.email).first()
    if test_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Email: {user.email} Already Taken")

    test_user = db.query(models.User).filter(models.User.username == user.username).first()
    if test_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Username: {user.username} Already Taken")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.get('{id}', response_model=schemas.UserOut)
def get_user(user_id: UUID, db: Session = Depends(get_db), current_user: UUID = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user