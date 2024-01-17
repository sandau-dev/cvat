# Provision new user(s) in the CVAT instance
#
# Schema:
# {
#   "username": "string",
#   "email": "user@example.com",
#   "password1": "string",
#   "password2": "string",
#   "first_name": "string",
#   "last_name": "string"
# }

from pprint import pprint
import csv
import os

from cvat_sdk.api_client import Configuration, ApiClient, exceptions
from cvat_sdk.api_client.models import *

# Read in a CSV file with the following columns:
# username, email, password1, password2, first_name, last_name, is_staff, is_superuser, is_active

# Set up an API client
# Read Configuration class docs for more info about parameters and authentication methods
configuration = Configuration(
    host = "https://asbuilt.cvat.sandau.dev",
    username = os.environ["CVAT_ADMIN_USERNAME"],
    password = os.environ["CVAT_ADMIN_PASSWORD"],
)

CVAT_ORGANIZATION = os.environ["CVAT_ORGANIZATION"]

with open('scripts/users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader):
        print(row['username'], row['email'], row['password1'], row['password2'], row['first_name'], row['last_name'], row['groups'], row['is_staff'], row['is_superuser'], row['is_active'], row['organization'], row['org_role'])

        with ApiClient(configuration) as api_client:
        #     # Create a new user
        #     register_serializer_ex_request = RegisterSerializerExRequest(
        #         username=row['username'],
        #         email=row['email'],
        #         password1=row['password1'],
        #         password2=row['password2'],
        #         first_name=row['first_name'],
        #         last_name=row['last_name'],
        #     ) # RegisterSerializerExRequest |

        #     try:
        #         (data, response) = api_client.auth_api.create_register(
        #             register_serializer_ex_request,)
        #         pprint(data)
        #     except exceptions.ApiException as e:
        #         print("Exception when calling AuthApi.create_register(): %s\n" % e)

        #     # Update the user's permissions
        #     id = 1 + idx # int | A unique integer value identifying this user.
        #     patched_user_request = PatchedUserRequest(
        #         username=row['username'],
        #         first_name=row['first_name'],
        #         last_name=row['last_name'],
        #         email=row['email'],
        #         groups=[group for group in row['groups'].split(',')],
        #         is_staff=bool(row['is_staff']),
        #         is_superuser=bool(row['is_superuser']),
        #         is_active=bool(row['is_active']),
        #     ) # PatchedUserRequest |  (optional)

        #     try:
        #         (data, response) = api_client.users_api.partial_update(
        #             id,
        #             patched_user_request=patched_user_request,
        #         )
        #         pprint(data)
        #     except exceptions.ApiException as e:
        #         print("Exception when calling UsersApi.partial_update(): %s\n" % e)

            invitation_write_request = InvitationWriteRequest(
                role=RoleEnum(row['org_role']),
                email=row['email'],
            ) # InvitationWriteRequest |
            x_organization = CVAT_ORGANIZATION # str | Organization unique slug (optional)

            try:
                (data, response) = api_client.invitations_api.create(
                    invitation_write_request,
                    x_organization=x_organization
                )
                pprint(data)
            except exceptions.ApiException as e:
                print("Exception when calling InvitationsApi.create(): %s\n" % e)
