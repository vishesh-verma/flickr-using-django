from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from external_data_sources.functions.internal import get_data_through_parameter
from external_data_sources.functions.internal import populate_data_to_groups_and_photos
from django.core.exceptions import ObjectDoesNotExist

@permission_classes([IsAuthenticated,])
@api_view(['POST'])
def load_data(request):
    """
    This function view gets hit by load_data api where we can send method, parameter_type and parameter as body.

    In our case method is flickr.groups.pools.getPhotos since we are pulling photos from group_id
    parameter_type is "group_id" and parameter will be id of the group.

    this api can be used for other cases as well such as if we need to collect group details from urls,tags
    and pull the photos as desired.

    """
    user = request.user
    request_data = request.data
    flickr_group_method = request_data["method"]
    parameter_type = request_data["type"]
    group_id = request_data["parameter"]
    data = get_data_through_parameter(flickr_group_method, parameter_type, group_id)# I tried to keep this function centralised so that it can be used multiple times
    if data.get('stat') == "fail":
        return Response(data["message"], status.HTTP_400_BAD_REQUEST)
    photos = data.get("photos")
    photo_list = photos.get("photo")
    if not photo_list:
        return Response("photos not found",status.HTTP_400_BAD_REQUEST)
    response_data, response_status = populate_data_to_groups_and_photos(user, group_id, photo_list)
    return Response(response_data, response_status)
