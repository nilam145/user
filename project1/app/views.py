from .models import (
    Organization,
    UserProfile,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    Organizationserializer,
    UserProfileserializer,
)
from django.http import Http404
from django.db import transaction

class MasterOrganizationList(APIView):

    def get(self, request, *args, **kwargs):
        orgs = Organization.objects.all()
        master_organizations = Organizationserializer(
            orgs,
            many=True,
        ).data
        return Response(master_organizations)


class MasterOrganizationDetails(APIView):
    def get(self, request, org_id, *args, **kwargs):
        print('i am in get')
        try:
            org = Organization.objects.get(id=org_id)
        except Organization.DoesNotExist:
            raise Http404(f"Organization does not exist with this id {org_id}")
        master_organization = Organizationserializer(
            org,
        ).data
        return Response(master_organization)

    def delete(self, request, org_id, *args, **kwargs):
        print('i am in delete')
        try:
            org = Organization.objects.get(id=org_id)
        except Organization.DoesNotExist:
            raise Http404(f"Organization does not exist with this id {org_id}")
        master_organization = Organizationserializer(
            org,
        ).data
        with transaction.atomic():
            org.delete()
        return Response(master_organization)


class MasterUserProfileList(APIView):

    def get(self, request, *args, **kwargs):
        users = UserProfile.objects.all()
        master_userprofiles = UserProfileserializer(
            users,
            many=True,
        ).data
        return Response(master_userprofiles)


class MasterUserProfileDetails(APIView):
    def get(self, request, user_id, *args, **kwargs):
        print('i am in get')
        try:
            user = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            raise Http404(f"UserProfile does not exist with this id {user_id}")
        master_userprofile = UserProfileserializer(
            user,
        ).data
        return Response(master_userprofile)

    def delete(self, request, user_id, *args, **kwargs):
        print('i am in delete')
        try:
            user = UserProfile.objects.get(id=user_id)
        except UserProfile.DoesNotExist:
            raise Http404(f"UserProfile does not exist with this id {user_id}")
        master_userprofile = UserProfileserializer(
            user,
        ).data
        with transaction.atomic():
            user.delete()
        return Response(master_userprofile)
