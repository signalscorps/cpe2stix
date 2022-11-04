# Backends

Backends allow you to store STIX Objects in a database of your choice in addition to the local filesystem. This section of the documentation shows available backends and how to configure them.

## Backend struture

Each Backend ships with a default initialization script that is used to create the database schema cve2stix will write to. This is executed the first time the backend is used.

Backends authentication is specified using a backend `<CONFIG>.yml`.

This configoration file is passed when running cve2stix commands.

## Local filesystem

The default backend is filesystem storage.

The Software SCOs are organised by vendor and product as follows;

* `stix2_objects/`
	* `software`
		* `software-ID`
			* `version`
* `stix2_bundles/`
	* `<VENDOR>`
		* `<PRODUCT>`
			* `bundle`
					* _Only contains most recent latest versions of vendor/product software objects. Note, in many case multiple versions, languages, etc software exist and each unique combination will be included in the bundle. Each time an object in a bundle is updated (or new object added), a new bundle is generated (with new `id`). Only latest bundle version exists in this directory.__

This backend is always used as the json files saved are used to populate other backends.