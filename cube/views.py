from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import datetime

from .models import Cell


# Create your views here.
class UploadView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'upload.html', context=None)

    def post(self, request, **kwargs):
        file_data = request.FILES['data_file'].read().decode("utf-8")
        lines = file_data.split('\n')
        for line in lines[:-1]:
            content = line.split('\t')
            if len(content) < 3:
                continue

            cell_id = int(content[0])
            cell_date = datetime.datetime.strptime(content[1], '%m/%d/%Y')
            cell_county = content[2]
            cell = Cell(id=cell_id, date=cell_date, county=cell_county)
            cell.save()

        return HttpResponse("")
