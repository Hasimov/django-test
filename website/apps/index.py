from django.http import JsonResponse


def api(response):
    json = {
        'foo': 'bar'
    }
    return JsonResponse(json)