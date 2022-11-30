from .models import Classifypro

def classification_links(request):
    links=Classifypro.objects.all()
    return dict(links=links)