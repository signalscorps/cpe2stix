# cpe2stix

![](/docs/assets/img/stix-cpe-graph.jpeg)

Turn CPEs managed by the National Vulnerability database into STIX 2.1 Objects.

## cpe2stix-output (avoid having to use this script)

This repository has a number of Github actions that run daily to populate [cpe2stix-output](https://github.com/signalscorps/cpe2stix-output) with historical CPE data (updated daily).

## Prerequisties

To use cpe2stix you will need to obtain a free API key from NVD.

[You can get one here](https://nvd.nist.gov/developers/start-here).

## Usage

This repository has been built with Github actions (to populate [cpe2stix-output](https://github.com/signalscorps/cpe2stix-output)). If you want to understand how this works, [please read the documentation here](/docs/github-actions).

To run the script locally;

### 1. Add API Key

Once you have your key, create a file in the root of this repository by copying the `nvd-credentials.yml.schema` to a new file called `nvd-credentials.yml`. Enter your API key for the variable `nvd_api_key` in this file.

### 2. Set variable

TODO

### 3. Run the script

TODO

## Documentation

Please take a moment to review the comprehensive documentation included in this repository -- it covers almost all common questions people have about cpe2stix.

[Read the documentation here](https://signalscorps.github.io/cpe2stix/).

## Support

[Signals Corps are committed to providing best effort support via Slack](https://join.slack.com/t/signalscorps-public/shared_invite/zt-1exnc12ww-9RKR6aMgO57GmHcl156DAA).

If you notice a bug or have a feature request, [please submit them as issues on Github](https://github.com/signalscorps/cpe2stix/issues).

## License

[MIT LICENSE](/LICENSE).

## A special thanks to...

I would like to thank the authors of the following tools used to build file2stix (making it a hundred times easier to do so);

* [STIX 2](https://pypi.org/project/stix2/): APIs for serializing and de-serializing STIX2 JSON content
* [STIX Viewer](https://github.com/traut/stixview): Quickly load bundles produced from your report.