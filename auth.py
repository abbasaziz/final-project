import json
from functools import wraps
from urllib.request import urlopen
from dotenv import load_dotenv
from flask import request
from jose import jwt
from os import environ

load_dotenv()

ALGORITHMS = environ.get('ALGORITHMS')
API_AUDIENCE = environ.get('API_AUDIENCE')
AUTH0_DOMAIN = environ.get('AUTH0_DOMAIN')

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_auth_token_header():
    authorization = request.headers.get('Authorization', None)

    if not authorization:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is missing.'
        }, 401)

    parts = authorization.split(' ')

    if parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Bearer should start Authorization header'
        }, 401)

    if len(parts) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)

    token = parts[1]

    return token


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permission not found in JWT.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'You are not allowed to perform this permission'
        }, 403)

    return True


def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    unverified_header = jwt.get_unverified_header(token)

    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization is malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e'],
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f'https://{AUTH0_DOMAIN}/',
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please check audience'
            }, 401)

        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Failed to parse the auth header'
            }, 400)

    raise AuthError({
        'code': 'invalid_header',
        'description': 'Could not find RSA key'
    }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_auth_token_header()
            try:
                payload = verify_decode_jwt(token)
            except BaseException as e:
                print(e)
                raise AuthError({
                    'code': 'invalid_token',
                    'description': 'Token is not valid.'
                }, 401)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
