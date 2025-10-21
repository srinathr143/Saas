from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def olddemo(request, *args, **kwargs):
    html_path = this_dir / "index.html"
    html_ = html_path.read_text()
    
    return HttpResponse(html_)

def demo(request):
    qs = PageVisit.objects.all()
    ps = PageVisit.objects.filter(path = request.path)
    path = request.path
    print('path',path)
    my_page = "srinath's"
    data = {
        "page":my_page,
        "total_count":qs.count(),
        "path_count":ps.count(),
        "percent":qs.count()*100.0 / ps.count(),
    }
    PageVisit.objects.create(path =path)
    return render(request, "index.html", data)