from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError



# Custom exception handler for JWT and application errors to provide clearer error messages for authentication issues.

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if isinstance(exc, (InvalidToken, TokenError)):
        return Response({"error": "Invalid or expired token. Please log in again."}, status=status.HTTP_401_UNAUTHORIZED)

    if response is not None:
        return response

    return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
