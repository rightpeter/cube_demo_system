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
        print(request.POST)
        print("files len: ", len(request.FILES))
        print(request.FILES['data_file'])

        file_data = request.FILES['data_file'].read().decode("utf-8")
        print(file_data)
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
