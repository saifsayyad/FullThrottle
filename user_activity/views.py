from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from user_activity.models import User, ActivityPeriod
import os
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def __upload_helper(uploaded_file):
    upload_dest = f'user_activity/static/uploads/{uploaded_file.name}'
    with open(upload_dest, 'wb') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)
    return os.path.abspath(upload_dest)


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['fileToUpload']
        try:
            upload_dest = __upload_helper(uploaded_file)
            rr = call_command('import_data_json', upload_dest)
            print(rr)
            return render(request, "upload.html", {'fileupload': 'Success'})
        except Exception as e:
            return render(request, "upload.html", {'fileupload': f'Upload failed - {str(e)}'})
    else:
        return render(request, "upload.html")


def get_data(request):
    user_data = User.objects.all()
    response = {'ok': True, 'members': []}
    for user in user_data:
        user_activity = dict()
        user_activity['id'] = user.id
        user_activity['real_name'] = user.real_name
        user_activity['tz'] = user.tz

        user_activity['activity_periods'] = []
        activities = ActivityPeriod.objects.filter(user=user)
        for activity in activities:
            temp = dict()
            temp['start_time'] = activity.start_time
            temp['end_time'] = activity.end_time
            user_activity['activity_periods'].append(temp)

        response['members'].append(user_activity)
    return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
