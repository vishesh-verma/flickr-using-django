
Note- For Authentication I have used JWTAuthentication of Django rest framework,
Note- I have used postman for testing the apis I recommend to use postman for testing.

1)Directions to use login api -
->give the url in postman http://127.0.0.1:8000/api/v1/login -> give username and password in Json format
in the body -> hit send with post method -> it gives you the access token and refresh token!
 you are good to go now and use the access token to access other apis

 Note-logout has not been implemented I have used JWTAuthentication
  The access token will expire automatically after its lifetime gets over.
  we can explicitly set the lifetime for access token or can be destroyed by the client.

2)Directions to use the other apis-
goto postman -> hit any of the provided api Ex:-http://127.0.0.1:8000/api/v1/groups/ -> give the headers
as:
       key             value
  √ Authorization     JWT "copy the access token got from the login api"
  √ Content-Types     application/json

once the headers are given go ahead and hit send with respective request type("GET","POST","DELETE","PATCH").

3)All the apis can only be accessed by the authenticated user.

4)The APIs are properly paginated with PAGE_SIZE = 30.

5)DRF routers are used to configure all your APIs.

6)APIs are versioned with REST API version based on Django rest framework.
the first version is the base. directory pattern -> api/base/urls for first version
                                                    api/v2/urls for the next version and so on...
7)I have tried to use the simplest Model, Serializer, and ViewSet with a very less no. of lines
of code delivering all the desired api's

8)requirements.txt is been added with all the dependencies.
Important Note- please create the virtual environment with python3. -> virtualenv -p python3 envname

9)The database is populated with 5 groups and 500 photos with a single user.


List of API's
  1.http://127.0.0.1:8000/api/v1/groups  - [GET]  all groups-list  #only authenticated user
  2.http://127.0.0.1:8000/api/v1/groups/<group_id>  - [GET, PATCH, DELETE]  group-detail #only authenticated user
      Ex: http://127.0.0.1:8000/api/v1/groups/82719930@N00  id is valid, can try the same url.

  3.http://127.0.0.1:8000/api/v1/group/<group_id> - [GET] photo ids of the group  #only authenticated user
      Ex: http://127.0.0.1:8000/api/v1/group/82719930@N00  id is valid, can try the same url.

  4.http://127.0.0.1:8000/api/v1/photos  - [GET] all photos-list  #only authenticated user
  5.http://127.0.0.1:8000/api/v1/photos/<photo_id>  - [GET, PATCH, DELETE] photo-details #only authenticated user
      Ex: http://127.0.0.1:8000/api/v1/photos/47531415092   id is valid, can try the same url.

  6.http://127.0.0.1:8000/api/v1/photos?group=<group_id>  - [GET]  photos-list of the group #only authenticated user
      Ex: http://127.0.0.1:8000/api/v1/photos?group=82719930@N00  id is valid, can try the same url

  7.http://127.0.0.1:8000/api/v1/login  [POST] login and get access token and refresh token
    login credentials:-
     {
     "username": "vishesh"
     "password": "Gh00st"
     }
     headers:-
     key             value
√ Content-Types     application/json

  Bonus API:-
        http://127.0.0.1:8000/api/v1/load_data - [POST] populate database by the group,
         photos under the group and associates the current authenticated user to the group

         body-

         {
	        "method": "flickr.groups.pools.getPhotos",
	         "type": "group_id",
	         "parameter": "1575180@N21" # use some other group id from flicker this one is already used
          }

          -method is the flickr  APIs methods,
          -type is parameter type like url,tgas,group_id,photo_id etc.according to the flickr api method
          -parameter is the value of the type Ex: 1575180@N21  which is a group id.

          Note - currently this api is works for  flickr.groups.pools.getPhotos method
          which only pulls photos by group id

          In order to make it work for other methods we just need to write handler for that.
          this does not changes the architecture of it.

Last Note- please do contact me for any doubts or queries this project is completely functional
           in my local machine.
