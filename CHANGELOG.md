# DocuSign Admin Python Client Changelog
All notable changes to this project will be documented in this file.

See [DocuSign Support Center](https://support.docusign.com/en/releasenotes/) for Product Release Notes.

## [v2.0.0rc2] - Admin API v2.1-1.4.1 - 2024-10-22
### Changed
- Added support for version v2.1-1.4.1 of the DocuSign Admin API.
- Removed the staging base path and OAuth path constant.
- Updated the SDK release version.

## [v2.0.0rc1] - Admin API v2.1-1.4.0 - 2024-08-27
### Breaking Changes
<details>
<summary>API Changes (Click to expand)</summary>

<br/>
<div style="margin-left: 20px;">

Added new query parameter "include_ds_groups" to the API "/v2/organizations/{organizationId}/users":

<h3>Added New APIs for Account Creation</h3>
<li>GET: get subscription details for organization</li>
<li>POST: initiate Create account request</li>
<li>GET: get ongoing process details by org ID</li>
<li>GET: get individual process details by org ID, asset group ID, asset group work ID</li>


</div>
</details>

- Deprecated nose library in favor of pynose.
 
### Other Changes
- Revised the logic to determine the `oauth_host_name` based on the `base_path`.
- Excluded test directories from package distribution.
- Added support for proxy HTTP connections.
- Adjusted the minimum required `PyJWT` package version to `2.0.0`.
- Added support for version v2.1-1.4.0 of the DocuSign Admin API.
- Updated the SDK release version.

## [v1.4.1] - Admin API v2.1-1.3.0 - 2023-11-13
### Changed
- Fixed installation steps in README.md
- Fixed link to API information in README.md
- Updated Travis CI URL in README.md
- Updated Python package URL in README.md

This commit addresses inconsistencies and outdated information in the documentation,
ensuring accurate and up-to-date details for users and contributors.

## [v1.4.0] - Admin API v2.1-1.3.0 - 2023-08-02
### Changed
- Added support for version v2.1-1.3.0 of the DocuSign Admin API.
- Updated the SDK release version.

New endpoints:
* `GET /v1/organizations/{organizationId}/assetGroups/accounts` Get asset group accounts for an organization.
* `POST /v1/organizations/{organizationId}/assetGroups/accountClone` Clone an existing DocuSign account.
* `GET /v1/organizations/{organizationId}/assetGroups/accountClones` Gets all asset group account clones for an organization.
* `GET /v1/organizations/{organizationId}/assetGroups/{assetGroupId}/accountClones/{assetGroupWorkId}` Gets information about a single cloned account.
## [v1.3.0] - Admin API v2.1-1.2.0 - 2023-05-10
### Changed
- Added support for version v2.1-1.2.0 of the DocuSign Admin API.
- Updated the SDK release version.

## [v1.2.0] - Admin API v2.1-1.1.1 - 2023-03-22
### Changed
- Added support for version v2.1-1.1.1 of the DocuSign Admin API.
- Updated the SDK release version.

## [v1.1.1] - Admin API v2.1-1.1.0 - 2022-09-20
### Changed
- Added support for version v2.1-22.3.00.00 of the DocuSign ESignature API.
- Updated the SDK release version.
### Fixed
- Fixed missing client side validation flag.

## [v1.1.0] - Admin API v2.1-1.1.0 - 2022-04-26
### Changed
- Added support for version v2.1-1.1.0 of the DocuSign Admin API.
- Updated the SDK release version.

## [1.0.0] - Admin API v2.1-1.0.0 - 2021-09-16
### Changed
- Added support for version v2.1-1.0.0 of the DocuSign Admin API.
- Updated the SDK release version.


## [v1.0.0a0] - OrgAdmin API v2.0-1.0.2 - 2020-06-07
### Added
- First Alpha version of OrgAdmin API, supports DocuSign OrgAdmin
