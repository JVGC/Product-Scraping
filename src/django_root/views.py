from rest_framework import views
from rest_framework.response import Response


class HomeView(views.APIView):
    def get(self, _) -> Response:
        return Response(data="Fullstack Challenge 20201026")
