# Selenium Grid Testing

Using [Selenium Grid](https://www.seleniumhq.org/) and [Pytest](https://docs.pytest.org/en/latest/) to automate distributed integrated testing

## Installing

```
source scripts/install.sh
```

Alternatively, you can manually install using the following steps:

#### Install Python 2.7 and pip

This developer is too lazy to compile SeleniumBase with Python3 - will use 2.7 until someone else updates

#### Install [poetry](https://github.com/sdispater/poetry) 

```
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

#### Add Poetry to your PATH in shell config (~/.bashrc, ~/.zshrc)

```
export PATH=$PATH:$HOME/.poetry/bin
```

You may need to source the file for changes to take effect.


#### Install dependencies with Poetry

In the root directory of this project, run:

```
poetry install
```

#### Install resources

The selenium standalone driver and webdrivers are included in the `resources` directory.

Copy the webdrivers into a `$PATH` directory.

## Start a hub or node

To start a hub, execute

```
java -jar resources/selenium-server-standalone-3.141.59.jar -role hub -hubConfig scripts/config/hubconfig.json
```

To start a node, edit `scripts/config/node1config.json`, and replace `"hub": "http://localhost:4444",` with your hub IP address. Execute

```
java -jar resources/selenium-server-standalone-3.141.59.jar -role node -nodeConfig scripts/config/node1config.json
```

Likewise with node2.

## Running the tests

Run tests on the **hub machine** in another terminal window. DO NOT run this on node machines.

The script below runs all tests and cleans up python cache code

```
source scripts/run-test.sh
```

You can also run tests from the command line. To enter a virtualenv:

```
poetry shell
```

Run tests:

```
pytest
```

Where it runs all tests on Chrome and Firefox. `--browser` is a required argument that accepts a string of browser names split by ";". It is set automatically in `pytest.ini` but can be subject to change.

`pytest-xdist` is also installed and can be run or configured. ie:

```
pytest -n 4
``` 

## Node Configuration

See [Selenium - Desired Capabilities](https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities)

## TODO

* Run tests concurrently
* Optimize configuration files and add scripts
* Dockerfile for scaling