from django.http import JsonResponse
from django.views import View
from .models import Author
import json

class AuthorListView(View):
    def get(self, request):
        authors = list(Author.objects.values())
        return JsonResponse(authors, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        author = Author.objects.create(**data)
        return JsonResponse({
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "bio": author.bio,
            "birth_date": author.birth_date
        })

class AuthorDetailView(View):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            return JsonResponse({
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
                "bio": author.bio,
                "birth_date": author.birth_date
            })
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

    def put(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(author, key, value)
            author.save()
            return JsonResponse({
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
                "bio": author.bio,
                "birth_date": author.birth_date
            })
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return JsonResponse({"deleted": True})
        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)
