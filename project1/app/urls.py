from django.urls import path
from .views import (
    MasterOrganizationList,
    MasterOrganizationDetails
)
from .views import (
    MasterUserProfileList,
    MasterUserProfileDetails
)

urlpatterns = [

    path(
          'orgs/<int:org_id>/',
          MasterOrganizationDetails.as_view(),
          name="details",
    ),

    path(
        'orgs',
        MasterOrganizationList.as_view(),
        name='list',
    ),

    path(
        'users/<int:user_id>/',
        MasterUserProfileDetails.as_view(),
        name='details',
    ),

    path(
        'users',
        MasterUserProfileList.as_view(),
        name='list',
    ),
]
