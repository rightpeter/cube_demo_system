from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class UploadView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'upload.html', context=None)
