from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('La hora de mi servidor es {now}'.format(now=now))


def sorted_v1(request):
    # import pdb
    # pdb.set_trace()
    from django.http import JsonResponse
    numbers = request.GET.get('numbers').split(',')
    numbers_int = [int(i) for i in numbers]
    sorted_int = sorted(numbers_int)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Integers sorted successfully'
    }
    return JsonResponse(data)


def sorted_v2(request):
    # import pdb
    # pdb.set_trace()
    numbers = request.GET.get('numbers').split(',')
    numbers_int = [int(i) for i in numbers]
    sorted_int = sorted(numbers_int)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=2), content_type='application/json')


def welcome(request, name, age):
    if age < 12:
        message = 'Sorry {}!, you are not allowed here'.format(name)
    else:
        message = 'Wellcome {}!, you are not allowed here'.format(name)
    return HttpResponse(message)
