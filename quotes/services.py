from quotes.models import Resource

def get_resources():
    return Resource.objects.filter(active=True)