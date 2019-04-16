import requests
import json
from rest_framework import status
from flickr.settings import flickr_api_key # This has to be imported as djnago.conf import settings, when working with two settings file for staging and prod
from flickr.settings import flickr_base_url
from gallery.api.base.serializer import GroupSerializer
from gallery.api.base.serializer import PhotoSerializer

def get_data_through_parameter(method, parameter_type, parameter):
    """This function takes the method, parameter-type and parameter and returns the required data using
    flickr api
    Example:- method: "flickr.urls.lookupGroup"
              type: "url"
              parameter: "https://www.flickr.com/groups/1540320@N21/"
    """

    url = flickr_base_url + "?method="+ method + "&api_key=" + flickr_api_key + "&" + parameter_type + "=" + parameter + "&format=json&nojsoncallback=1"
    r = requests.get(url=url)
    data = r.json()
    return data

def populate_data_to_groups_and_photos(user, parameter, photo_list):
     """
     This function takes theuser, group data and photo data, associates user to groups, group to the photos and
     populate the data through serializers
     """

     group_data = get_data_through_parameter("flickr.groups.getInfo", "group_id", parameter)
     group_name = group_data["group"]["name"]["_content"]
     dict_for_group = {"group_id": parameter, "group_name": group_name, "user": user.id}
     group_serializer = GroupSerializer(data=dict_for_group)
     if not group_serializer.is_valid():
         return group_serializer.errors, status.HTTP_400_BAD_REQUEST
     group_object = group_serializer.save()
     for object in photo_list:
         object["group"] = group_object.group_id
     photo_serializer = PhotoSerializer(data=photo_list, many=True)#bulk create for photos under teh group
     if not photo_serializer.is_valid():
         return photo_serializer.errors, status.HTTP_400_BAD_REQUEST
     photo_serializer.save()
     return GroupSerializer(group_object).data, status.HTTP_201_CREATED
