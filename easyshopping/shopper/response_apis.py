import json
import simplejson
from django.http import JsonResponse


def response_api(func):
    """ Renders JsonResponse objects. """

    def wraps(*args, **kwargs):

        # Retrieving request from args
        request = args[0]

        # Applying initial settings for lazy load
        start = int(request.GET.get('start') or 0)
        end = int(request.GET.get('end') or start)

        # Applying SQL request
        query = func(*args, **kwargs)

        # Creating json data
        json_objects = simplejson.dumps([item for item in query])

        json_data = json.loads(json_objects)

        # Creating list and fill it by objects
        data = []
        try:
            for i in range(start, end):
                data.append(json_data[i])
        except IndexError as i:
            print(i)

        return JsonResponse(
            {
                'products': data,
                'length': len(json_data),
            },
        )

    return wraps

def response_api_card_item(func):

    def wraps(*args, **kwargs):

        query = func(*args, **kwargs)

        json_objects = simplejson.dumps([item for item in query])

        json_data = json.loads(json_objects)

        return JsonResponse(
            {'items': json_data}
        )

    return wraps