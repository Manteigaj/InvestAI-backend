from app.core.security import hash_password, verify_password

password = "senha12345"

hashed_password = hash_password(password)

print(f'hashed_password: {hashed_password}')

verify_password = verify_password(password, hashed_password)

print(f'verify_password: {verify_password}')

