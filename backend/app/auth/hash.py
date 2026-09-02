from passlib.context import CryptContext



PwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return PwdContext.hash(password)

    def verify(hashed_password, plain_password):
        return PwdContext.verify(plain_password, hashed_password)