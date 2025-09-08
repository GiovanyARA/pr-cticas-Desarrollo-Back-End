from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status as drf_status

def custom_exception_handler(exc, context):
    # Intenta dejar que DRF maneje el error primero
    response = exception_handler(exc, context)

    if response is not None:
        # Normalizamos el formato de error
        data = {
            "ok": False,
            "detail": response.data,
        }
        return Response(data, status=response.status_code)

    # Errores no controlados
    return Response(
        {"ok": False, "detail": "Error interno del servidor"},
        status=drf_status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
