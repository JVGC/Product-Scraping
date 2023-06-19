""" Django Root Views """
from rest_framework import views
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class HomeView(views.APIView):
    """Django Home View"""

    @extend_schema(tags=["Home"])
    def get(self, _) -> Response:
        """GET Home Method
        Returns the message: Fullstack Challenge 20201026
        """
        return Response(data="Fullstack Challenge 20201026")
