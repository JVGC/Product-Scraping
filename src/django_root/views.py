""" Django Root Views """
from rest_framework import views
from rest_framework.response import Response


class HomeView(views.APIView):
    """Django Home View"""

    def get(self, _) -> Response:
        """GET Home Method
        Returns the message: Fullstack Challenge 20201026
        """
        return Response(data="Fullstack Challenge 20201026")
