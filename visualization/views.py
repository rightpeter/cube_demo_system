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
                if location in svgPath:
                    paths.append(svgPath[location])
            return paths

        directoryPath = 'cube_demo_system/static/json/'
        with open(directoryPath + 'topic.json') as topicFile, open(directoryPath + 'county.json') as locationFile, open(directoryPath + 'time.json') as timeFile:
            topic = json.load(topicFile)
            location = json.load(locationFile)
            time = json.load(timeFile)
        raw = list(map(lambda news: {'time': news[2], 'location': getSVGPath(news[1].keys()), 'topics': news[0]}, zip(topic, location, time)))
        for i in raw:
            i['time'] = datetime.strptime(i['time'], "%Y.%m.%d")
        # minDate = min(raw, key=lambda x: x['time'])['time']
        minDate = datetime.strptime('2018.11.07', "%Y.%m.%d")

        for i in raw:
            i['time'] = (i['time'] - minDate).days
        maxDate = max(raw, key=lambda x: x['time'])['time']

        with open('cube_demo_system/static/json/cell_key_sentence.json') as keySentenceFile:
            summary = json.load(keySentenceFile)

        with open('cube_demo_system/static/json/image_county.json') as imageFile:
            image = json.load(imageFile)

        return render_to_response(
            'visualization/county.html', {
                'minDate': minDate.strftime('%B %d, %Y'),
                'dateRange': maxDate,
                'fireData': raw,
                'summary': summary,
                'image': image
            })


class CityView(TemplateView):

    def get(self, request, **kwargs):
        topic = request.GET.get('topic')
        county = request.GET.get('county')
        date_period = request.GET.get('time')

        with open('cube_demo_system/static/geo/butte.geojson') as f:
            butte = json.load(f)

        with open('cube_demo_system/static/geo/butte-city.geojson') as f:
            butte_city = json.load(f)

        with open('cube_demo_system/static/json/cell_key_sentence_city.json') as keySentenceFile:
            summary = json.load(keySentenceFile)

        with open('cube_demo_system/static/json/image_city.json') as imageFile:
            image = json.load(imageFile)

        return render_to_response(
            'visualization/city.html', {
                'topic': topic,
                'county': county,
                'date_period': date_period,
                'butte': butte,
                'butte_city': butte_city,
                'summary': summary,
                'image': image
            })
