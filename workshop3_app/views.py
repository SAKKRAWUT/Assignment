from django.shortcuts import render
from .models import Movie,Attend

from django.http import HttpResponseRedirect, HttpResponse
import json
# Create your views here.
def homepage(request):
    context = {
        'vaar1': 'This is to handle inpput',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def Movie_list(request):
    #qs = PlayVideo.objects.all()
    list = [{'id': x.Movie_id, 'title': x.Movie_name,'unit': x.Movie_year, 'genre': x.genre,

         }
            for x in Movie.objects.filter(void=0).order_by('-created_time')]
    #qs_json = serializers.serialize('json', list)
    qs_json = json.dumps(list)
    return HttpResponse(qs_json, content_type='application/json')


def Movie_detail(request):
    id = request.GET.get('id')
    list = [{

             'id': x.Movie_id, 'title': x.Movie_name,
        'unit': x.Movie_year, 'genre': x.genre,
             'updated_time': x.updated_time.strftime('%Y-%m-%d %H:%M:%S'),
             'created_time': x.created_time.strftime('%Y-%m-%d %H:%M:%S'),
             }
            for x in Movie.objects.filter(Movie_id=id).filter(void=0).order_by('-created_time')]


    qs_json = json.dumps(list[0])
    return HttpResponse(qs_json, content_type='application/json')


def attend_list(request):
    attendances_list = [
        {
            'ATTN_Number': attend.ATTN_Number,
            'Movie_Name': attend.movie_name.Movie_name,  # Accessing related Movie object
            'Seat_Number': attend.seat_number,
            'Show_Time': attend.show_time
        }
        for attend in Attend.objects.all().order_by('-ATTN_Number')
    ]

    return HttpResponse(json.dumps(attendances_list), content_type='application/json')


# Attendance Detail based on ATTN_Number
def attend_detail(request, attn_number):
    try:
        attend = Attend.objects.get(ATTN_Number=attn_number)
        attend_details = {
            'ATTN_Number': attend.ATTN_Number,
            'Movie_Name': attend.movie_name.Movie_name,  # Accessing related Movie object
            'Seat_Number': attend.seat_number,
            'Show_Time': attend.show_time
        }

        return HttpResponse(json.dumps(attend_details), content_type='application/json')

    except Attend.DoesNotExist:
        return HttpResponse(json.dumps({"error": "Attendance not found"}), content_type='application/json', status=404)



