import base64

from rest_framework import authentication, exceptions

from .settings import CLIENT_TOKENS


class BearerTokenAuthorization(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            authorization_header = request.META['HTTP_AUTHORIZATION']
            _, token_base64 = authorization_header.split(' ')
            client, password = token.split(':')
            if CLIENT_TOKENS[client] == password:
                return None, None
            else:
                raise exceptions.AuthenticationFailed("Invalid authentication token")
        except KeyError:
            raise exceptions.AuthenticationFailed("Missing authentication header")
        except IndexError:
            raise exceptions.AuthenticationFailed("Invalid authentication header")
