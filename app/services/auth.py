from sqlalchemy.testing.pickleable import User

from app.db.database import SessionLocal

def user_register(username, email ,password, session:SessionLocal):
    user = User(
        username=username,
        email=email,
    )

    