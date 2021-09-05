from django.shortcuts import render
from django.http  import HttpResponse
from . models import Location, Category, Image

# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request, "index.html", {"images":images})

def search_results(request):
    
    if "image" in request.GET and request.GET["image"]:
        search_word=request.GET.get("image")
        searched_image=Image.search_by_category(search_word)
        message=f"{search_word}"

        return render(request, 'search.html', {"message": message, "images":searched_image})

    else:
        message="You haven't searched for any image"
        return render(request, 'search.html', {"message":message})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'pictures/location.html', {'location_images': images})
