from app.core.security import hash_password, verify_password

def test_verify_password_correct():
    password = "password12345"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password)

def test_verify_password_incorrect():
    password = "password12345"
    hashed_password = hash_password(password)

    assert not verify_password("wrong-password", hashed_password)

def test_hash_password():
    password = "password12345"
    hashed_password = hash_password(password)

    assert hashed_password != password



