# PROBUS

[![codecov](https://codecov.io/github/royrusso/probus/graph/badge.svg?token=B972KDOOOB)](https://codecov.io/github/royrusso/probus)
![Tests](https://img.shields.io/github/actions/workflow/status/royrusso/probus/pytests_codecov.yml?label=Tests)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)

# This project is in early development!

A _FAST_ network monitor and UI that actively scans and alerts you
to network changes, new devices, open ports, and identifies CVEs
(Common Vulnerabilities and Exposures)

## Table of Contents

- [Introduction](#introduction)
  - [Features](#features)
- [Installation](#installation)
- [Development](#development)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Introduction

Probus is a network scanner that identifies security vulnerabilities in your network and alerts you to new ones as they arise. Probus scans your network quickly using a combination of Nmap and a 2-pass scanning technique to identify hosts and open ports.

Probus is platform-agnostic and available as a Docker container.

### Features:

- **Network Scanner:** Asynchronously scans your network for hosts and open ports.
- **Scheduled Scans:** Scans your network on a schedule.
- **Vulnerability Scanner:** Identifies security vulnerabilities in your network on a per-device basis.
- **Scan and Vulnerability History:** Keeps a history of scans and vulnerabilities identified.
- **Alerting:** Alerts you to new vulnerabilities as they arise, new devices added to your network, given a network range.
- **Platform agnostic**: Avilable as a docker container.

## Installation

Download the Docker from: TODO

UI is accessible from: [http://localhost:8080](http://localhost:8080).

Swagger API is accessible from: [http://localhost:8000/docs](http://localhost:8000/docs).

### Local Installation from Sources

Clone the repository. Then, run `docker compose up --build`.

## Development

Please read the [DEVELOPMENT.md](DEVELOPMENT.md) file for more information on how to run this project locally.

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to this project.

## Contact

- Use **GitHub Issues** for code-related issues.

## License

Probus is licensed under the [Apache License 2.0](LICENSE).
