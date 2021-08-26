# coding: utf-8

from __future__ import absolute_import, print_function
from docusign_admin import ApiException, AccountsApi, UsersApi, ProductPermissionProfilesApi, BulkImportsApi

import base64
import os
import unittest
import docusign_admin as docusign
import tempfile

Username = os.environ.get("USER_NAME")
IntegratorKey = os.environ.get("INTEGRATOR_KEY_JWT")
BaseUrl = "https://api-d.docusign.net/management"
OauthHostName = "account-d.docusign.com"
SignTest1File = "{}/docs/SignTest1.pdf".format(os.path.dirname(os.path.abspath(__file__)))
BulkImportFile = "{}/docs/bulk_import.csv".format(os.path.dirname(os.path.abspath(__file__)))
TemplateId = os.environ.get("TEMPLATE_ID")
UserId = os.environ.get("USER_ID")
PrivateKeyBytes = base64.b64decode(os.environ.get("PRIVATE_KEY"))
accountId = os.environ.get("ACCOUNT_ID")


class SdkUnitTests(unittest.TestCase):

    def setUp(self):
        self.api_client = docusign.ApiClient(base_path=BaseUrl, oauth_host_name=OauthHostName)
        self.api_client.rest_client.pool_manager.clear()

        docusign.configuration.api_client = self.api_client
        try:
            self.api_client.host = BaseUrl
            token = (self.api_client.request_jwt_user_token(client_id=IntegratorKey,
                                                            user_id=UserId,
                                                            oauth_host_name=OauthHostName,
                                                            private_key_bytes=PrivateKeyBytes,
                                                            expires_in=3600,
                                                            scopes=["signature", 'organization_read',
                                                                    'user_read','user_write']))
            self.user_info = self.api_client.get_user_info(token.access_token)
            self.api_client.rest_client.pool_manager.clear()
            docusign.configuration.api_client = self.api_client
            accounts_api = AccountsApi()
            organization = accounts_api.get_organizations()
            self.organization_id = organization.organizations[0].id
        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)
        self.api_client.rest_client.pool_manager.clear()

    def tearDown(self):
        self.api_client.rest_client.pool_manager.clear()

    def testOrgAdmin(self):
        try:
            accounts_api = AccountsApi()
            organizations = accounts_api.get_organizations()
            self.assertIsNotNone(organizations)

        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testCreateUser(self):
        try:
            users_api = UsersApi()
            permissionProfile = docusign.PermissionProfileRequest(id=9305351)
            account = docusign.NewUserRequestAccountProperties(id=self.user_info.accounts[0].account_id,
                                                                           permission_profile=permissionProfile)
            accounts = [account]
            request = docusign.NewUserRequest(user_name='testuser', email='xxx@yyy.zzz', accounts=accounts)
            res = users_api.create_user(organization_id=self.organization_id, request=request)
            self.assertIsNotNone(res)

        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)

    def testGetUserProfiles(self):
        try:
            users_api = UsersApi()
            profile = users_api.get_user_profiles(organization_id=self.organization_id, email='xxx@yyy.zzz')

            self.assertIsNotNone(profile)
        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)

    def testGetProductPermissionProfiles(self):
        try:
            permissions_api = ProductPermissionProfilesApi()
            permissions = permissions_api.get_product_permission_profiles(organization_id=self.organization_id,
                                                                      account_id=self.user_info.accounts[0].account_id)

            self.assertIsNotNone(permissions)
        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)

    def testBulkImport(self):
        try:
            with open(BulkImportFile, 'rb') as sign_file:
                file_contents = sign_file.read()
            sign_file.close()

            str_contents = file_contents.decode().replace('<accountId>', self.user_info.accounts[0].account_id).encode()
            temp = tempfile.NamedTemporaryFile(suffix='.csv')
            temp.write(str_contents)
            temp.seek(0)

            bulk_import_api = BulkImportsApi()
            response = bulk_import_api.create_bulk_import_add_users_request(organization_id=self.organization_id,
                                                                            file_csv=temp.name)

            self.assertIsNotNone(response)

        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)

    def testGetUsers(self):
        try:
            users_api = UsersApi()
            users = users_api.get_users(organization_id=self.organization_id,
                                          account_id=self.user_info.accounts[0].account_id)

            self.assertIsNotNone(users)
        except ApiException as e:
            print("\nException when setting up DocuSign OrgAdmin API: %s" % e)
        except Exception as e:
            print("\nException when calling DocuSign OrgAdmin API: %s" % e)

if __name__ == '__main__':
    unittest.main()
