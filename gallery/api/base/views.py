from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from gallery.models import Group
from gallery.api.base.serializer import GroupSerializer
from gallery.models import Photo
from gallery.api.base.serializer import PhotoSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes


class GroupViewSet(ModelViewSet):
    """
    This Viewset fulfils the following api requests
    1. api/v1/groups This API when called with the appropriate USER TOKEN using
    DRF token authentication will return all the groups that below to the user with
    details such as group name, group id, number of photos

    2. api/v1/groups/GID returns details of the group

    Possible response status:-
    1. 200 - returns the groups
    2. 404 - did not find the group in the data base
    3. 401 - Unauthorized only related user can access the data

    """
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(user=user)# so only user associated with the group can access the group record


class PhotoViewSet(ModelViewSet):
    """
    This Viewset fulfils the following api requests:

    /api/v1/photos/?group=<GID> -- This API when called with the appropriate USER
    TOKEN using DRF token authentication and supplying a group id will return all
    the photos belonging to the group

    /api/v1/photos/<ID> -- This API when called with the appropriate USER TOKEN
    using DRF token authentication should return details of the photo

    Possible response status:-
     1. 200 - returns the groups
     2. 404 - did not find the group in the data base
     3. 401 - Unauthorized only related user can access the data
    """

    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        group_id = self.request.query_params.get("group")
        if group_id:
            return Photo.objects.filter(group=group_id)
        else:
            return Photo.objects.filter(group__user=user)# so only user associated with the photos can access the photo record


@permission_classes([IsAuthenticated,])
@api_view(["GET"])
def get_photo_id(self, id):
    """
        This Viewset fulfils the following api requests:

    /api/v1/group/<ID> -- This API when called with the appropriate USER TOKEN
    using DRF token authentication will return all the photos <ID> belonging to the
    group

    Possible response status:-
    1. 200 - returns the pohot ids belonging to the group
    2. 404 - did not find the photo id's for group id
    3. 401 - Unauthorized only related user can access the group or photo data otherwise gives the anauthorized status
    """
    user = self.user
    print(id)
    photo_list = Photo.objects.filter(group=id)# so only user associated with the photos can access the photo record
    return Response(photo_list.values("id"))
