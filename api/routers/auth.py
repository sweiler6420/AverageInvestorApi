from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from uuid import UUID
import boto3

from ..config import settings
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/v1/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.username == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    # return token

    # Must convert UUID to string since UUID cannot be serialized
    user = str(user.user_id)

    # Encode user roles if we decide to add roles
    auth_payload = oauth2.create_access_token(data={"user_id": user})

    payload = {"access_token": auth_payload['access_token'], "token_type": "Bearer", "expire": auth_payload['expire']}

    return payload
