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
	* `<VENDOR>`
		* `<PRODUCT>`
			* `software`

This backend is always used as the json files saved are used to populate other backends.