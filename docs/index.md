# cve2stix Documentations

In short; cpe2stix converts CPEs from the NVD into STIX 2.1 Objects.

In this documentation you will find details of how this is performed.

For installation, [please see the README.md file at the root of cpe2stix](https://github.com/signalscorps/cve2stix).

## What's in the docs?

* [NVD API (CPE Download)](./nvd-api.md): cpe2stix downloads data from the NVD CPE API. This section of the documentation explains how backfill and updates happen.
* [Conversion to STIX 2.1](./stix-objects.md): cpe2stix converts all CPEs into a range of STIX Objects. This section of the documentation explains how STIX Objects are created.
* [Backends](./backends.md): Backends allow you to store STIX Objects in a database of your choice in addition to the local filesystem. This section of the documentation shows available backends and how to configure them.
* [Github Actions](./github-actions.md): This repository has been built with Github Actions (to populate [cpe2stix-output](https://github.com/signalscorps/cpe2stix-output)). This section of the documentation will explain how that's setup.

## Building these docs

You are probably reading this online (deployed via Github pages `.github/workflows/docs.yml`.

https://signalscorps.github.io/cpe2stix/

If you want to build the docs locally, from the root directory run;

```shell
pip3 install -r docs/requirements.txt
mkdocs serve --config-file mkdocs.yml
```