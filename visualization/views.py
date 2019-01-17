from django.shortcuts import render_to_response
from django.views.generic import TemplateView

import json
from datetime import datetime


# Create your views here.
class CountyView(TemplateView):

    def get(self, request, **kwargs):
        svgPath = {
            'Modoc': '_x30_49_Modoc',
            'Butte': '_x30_07_Butte',
            'Tehama': '_x31_03_Tehama',
            'Colusa': '_x30_11_Colusa',
            'Santa Clara': '_x30_85_Santa_Clara',
            'San Mateo': '_x30_81_San_Mateo',
            'Placer': '_x30_61_Placer',
            'Riverside': '_x30_65_Riverside',
            'Kern': '_x30_29_Kern',
            'Plumas': '_x30_63_Plumas',
            'Shasta': '_x30_89_Shasta',
            'Los Angeles': '_x30_37_Los_Angeles',
            'Siskiyou': '_x30_93_Siskiyou',
            'San Benito': '_x30_69_San_Benito',
            'San Francisco': '_x30_75_San_Francisco',
            'Sutter': '_x31_01_Sutter',
            'San Luis Obispo': '_x30_79_San_Luis_Obispo',
            'Orange': '_x30_59_Orange',
            'Monterey': '_x30_53_Monterey',
            'Tulare': '_x31_07_Tulare',
            'Del Norte 1 ': '_x30_15_Del_Norte_1_',
            'Mariposa': '_x30_43_Mariposa',
            'San Joaquin': '_x30_77_San_Joaquin',
            'Lake': '_x30_33_Lake',
            'Fresno': '_x30_19_Fresno',
            'Madera': '_x30_39_Madera',
            'Alameda': '_x30_01_Alameda',
            'Sonoma': '_x30_97_Sonoma',
            'Mono': '_x30_51_Mono',
            'Ventura': '_x31_11_Ventura',
            'Inyo': '_x30_27_Inyo',
            'Marin': '_x30_41_Marin',
            'Imperial': '_x30_25_Imperial',
            'Napa': '_x30_55_Napa',
            'Stanislaus': '_x30_99_Stanislaus',
            'Lassen': '_x30_35_Lassen',
            'San Bernardino': '_x30_71_San_Bernardino',
            'Tuolumne': '_x31_09_Tuolumne',
            'Mendocino': '_x30_45_Mendocino',
            'Calaveras': '_x30_09_Calaveras',
            'Solano': '_x30_95_Solano',
            'Santa Barbara': '_x30_83_Santa_Barbara',
            'Contra Costa': '_x30_13_Contra_Costa',
            'Humboldt': '_x30_23_Humboldt',
            'Sierra': '_x30_91_Sierra',
            'Glenn': '_x30_21_Glenn',
            'Yolo': '_x31_13_Yolo',
            'Merced': '_x30_47_Merced',
            'Yuba': '_x31_15_Yuba',
            'Amador': '_x30_05_Amador',
            'Nevada': '_x30_57_Nevada',
            'Santa Cruz': '_x30_87_Santa_Cruz',
            'Trinity': '_x31_05_Trinity',
            'El Dorado': '_x30_17_El_Dorado',
            'Alpine': '_x30_03_Alpine',
            'Sacramento': '_x30_67_Sacramento',
            'San Diego': '_x30_73_San_Diego'
        }

        def getSVGPath(locations):
            paths = []
            for location in locations:
                paths.append(svgPath[location])
            return paths

        with open('cube_demo_system/static/json/fg_title_text.json') as f:
            data = json.load(f)

        raw = list(map(lambda news: {'time': news[1], 'id': news[0].split('/')[-1], 'location': getSVGPath(news[4].keys()), 'topics': news[6]}, data))
        #     raw = [{'time':'2018.11.10', id:'1', 'location':'_x30_07_Butte', 'topics':[0,0,1]},
        #            {'time':'2018.11.11', id:'2', 'location':'_x31_03_Tehama', 'topics':[0,1,0]},
        #            {'time':'2018.11.12', id:'3', 'location':'_x30_07_Butte', 'topics':[1,0,0]},
        #            {'time':'2018.11.11', id:'4', 'location':'_x31_03_Tehama', 'topics':[1,0,0]},
        #            {'time':'2018.11.13', id:'5', 'location':'_x30_07_Butte', 'topics':[0,1,0]},
        #            {'time':'2018.11.17', id:'6', 'location':'_x31_03_Tehama', 'topics':[0,1,0]},
        #            ]
        for i in raw:
            i['time'] = datetime.strptime(i['time'], "%Y.%m.%d")
        minDate = min(raw, key=lambda x: x['time'])['time']
        for i in raw:
            i['time'] = (i['time'] - minDate).days
        maxDate = max(raw, key=lambda x: x['time'])['time']
        return render_to_response(
            'visualization/county.html', {
                'minDate': minDate.strftime('%B %d, %Y'),
                'dateRange': maxDate,
                'data': raw
            })


class CityView(TemplateView):

    def get(self, request, **kwargs):
        with open('cube_demo_system/static/geo/butte.geojson') as f:
            butte = json.load(f)

        with open('cube_demo_system/static/geo/butte-city.geojson') as f:
            butte_city = json.load(f)

        return render_to_response('visualization/city.html', {
            'butte': butte,
            'butte_city': butte_city,
        })
