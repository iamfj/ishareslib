# ishareslib

[![Codecov](https://img.shields.io/codecov/c/github/iamfj/ishareslib?label=Code%20Coverage&logo=codecov&logoColor=fff)](https://codecov.io/gh/iamfj/ishareslib)
[![Quality Workflow](https://github.com/iamfj/ishareslib/actions/workflows/quality.yml/badge.svg)](https://github.com/iamfj/ishareslib/actions/workflows/quality.yml)
[![Integration Workflow](https://github.com/iamfj/ishareslib/actions/workflows/integrate.yml/badge.svg)](https://github.com/iamfj/ishareslib/actions/workflows/integrate.yml)

The ishareslib is a library that simplifies the retrieval of data on the ishares product family in python.

By reverse engineering a clear interface was created to be able to process the data easily. During development, care was
taken to reduce the number of requests against the ishares server. In addition, custom adapters for user agent and proxy
server can be connected to disguise the traffic.

### Installing

```shell
pip install ishareslib
```

## Usage

This is how you use this interface in your environment:

```python
import Client
from ishareslib.client

client = Client()
client.get_products()  # This will be a pandas dataframe
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

What things you need to install the software and how to install them

```shell
pip install . .[dev] .[test]
```

## Running the tests

The tests are split into two groups unit tests (without explicit group) and integration test. The unit tests are started
with every pull request. The integration tests run time-controlled to detect a change of the ishares interfaces quickly
to be able to adapt the library.

How to run unit tests:

```shell
pytest -m "not integration"
```

How to run integration tests:

```shell
pytest -m "integration"
```

The coverage of the tests should always be above 90 percent. Please make sure that your tests are thorough and well
thought out.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see
the [tags on this repository](https://github.com/iamfj/ishareslib/tags)

## License

This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](LICENSE) file for details
