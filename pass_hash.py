import bcrypt

BCRYPT_ROUNDS = 12


def hash_password(password: str) -> str:
    if isinstance(password, str):
        password = password.encode("utf-8")

    hashed = bcrypt.hashpw(password, bcrypt.gensalt(BCRYPT_ROUNDS))
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    if isinstance(password, str):
        password = password.encode("utf-8")

    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password, hashed_password)
