import datetime
import jwt
import settings


def encode_jwt_token(data, expiration_time_seconds=60):
    payload = {
        **data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_time_seconds),
    }
    encoded_jwt = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )
    return encoded_jwt


def decode_jwt_token(encoded_token):
    decoded = jwt.decode(
        encoded_token,
        settings.JWT_SECRET,
        algorithms=["HS256"],
    )
    return decoded


data_to_encode = {"my_name": "Vasyl", "age": 10}
encoded_token = encode_jwt_token(data_to_encode)
print(encoded_token)

decoded_payload = decode_jwt_token(encoded_token)
print(decoded_payload)


