# Pet Store Testing Framework

### Table of Contents
[Overview and Tools](#overview-and-tools) <br>
[Project Structure](#project-structure) <br>
[Setup](#setup) <br>
[Running Tests](#running-tests) <br>
[Roadmap](#roadmap) <br>
[Related Links and Docs](#related-links-and-docs)


## Overview and Tools

Testing Framework for [JPetStore Demo UI](https://petstore.octoperf.com/actions/Catalog.action) and [Swagger Petstore](https://petstore.swagger.io/#/) API, as they are not linked they are tested separately. This is a personal project for learning purposes, I have no other relation to the actual system under test.

The current testing framework is developed with Python's [Pytest](https://docs.pytest.org/en/7.2.x/) testing framework, using [Requests](https://docs.python-requests.org/en/latest/index.html) for API testing, [Cerberus](https://docs.python-cerberus.org/en/stable/index.html) for Schema testing, and [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) for UI testing (Chrome only). UI tests are designed with a personalized POM pattern and a driver singleton instance. Both UI and API are tested with Data Driven Testing methodology.

## Project Structure
<pre>
pet-store-testing-framework
├── core
│   ├── pages UI pages using personalized POM design pattern.
│   ├── __init__.py 
│   ├── api_core.py Direct calls to the API with the basic verbs using Requests, returns a Response object or raises an error.
│   ├── custom_assertions.py For both UI and API tests.
│   └── element.py Added abstraction layer to POM pattern for web Element interaction, increasing modularity, readability, maintainability, and reuse.
├── helpers
│   ├── __init__.py
│   ├── base_wrapper.py API Core wrapper for including basic headers and parametrized URL path.
│   ├── pet_wrapper.py Personalized API calls for pet endpoint using base_wrapper, returns response object, and logs info.
│   ├── store_wrapper.py Personalized API calls for store endpoint using base_wrapper, returns response object, and logs info.
│   └── ui_helpers.py UI tests helpers, i.e. a class for user session management.
├── resources
│   ├── __init__.py
│   ├── driver.py Configured Chrome Web Driver for UI tests using the singleton pattern.
│   └── random_data_generator.py Returns useful random data, from random strings to invalid data generators for API endpoints.
├── tests Contains all the test suite.
│   ├── api_tests Contains all API tests: endpoints divided per file.
│   ├── ui_tests Contains all UI tests dividing features per file, contains a base test class with driver, pages, etc.
│   └── unit_tests Contains all unit tests.
├── utils
│   ├── __init__.py
│   ├── custom_strings.py For varied string processing, i.e. returning error name from an exception for logging purposes.
│   ├── get_data_set.py For different API payload generation and all pets available information for UI.
│   ├── get_schema.py schema dictionaries using Cerebrus syntax.
│   └── ui_utils.py Random UI utils, like enumerator for locator types.
├── .gitignore All files and directories ignored throughout the whole framework, like cache, venv, logs, etc.
├── config.py Basic config including URIs and logger configuration.
├── conftest.py Empty conftest to allow Pytest to find modules automatically.
├── README.md API 
└── requirements.txt
*Logs directory will be added automatically as well after running tests.
</pre>

## Setup
1. Install Python 3.10.
2. Clone this repository and move to it.
3. Create a virtual environment for Python running `python -m venv venv`
4. Activate the virtual environment:
   * On Windows: `venv\Scripts\activate.bat`
5. Install requirements: `pip install -r requirements.txt`

## Running Tests
This testing framework was designed to not contain obscure param information when running tests, so they can be run with Pytest 7 commands normally (see documentation).
Quick access basic commands:
*  Run full suite (API & UI): `pytest`
*  Run only API tests: `pytest tests/api_tests`
*  Run only UI tests: `pytest tests/ui_tests`
*  Run only unit tests: `pytest tests/unit_tests`
*  Run specific feature test (i.e. UI user): `pytest tests/ui_tests/test_user.py`
*  Run specific test (i.e. API store add order): `pytest tests/api_tests/test_store.py::test_add_order`

In the case of using Pycharm IDE, edit the runner to select the module name using the three dots on the left, or click the green arrow on each test/class to do it individually.

## Roadmap
While many goals have been accomplished, there are still extra functionalities I would like to keep adding as a personal project when time is available, including but not restricted to (in no particular order):
1. [ ] Incorporate Allure reports.
2. [ ] Integrate Jenkins.
3. [ ] Migrate Bug reporting from Google Docs to Trello/Jira Board.
4. [ ] Clean up and make a public test plan and strategy.
5. [ ] Keep adding API and UI tests.
6. [ ] Pipeline: TBD after free GitHub actions capabilities research.

## Related Links and Docs
* [WebSite under test](https://petstore.octoperf.com/actions/Catalog.action).
* [API under test](https://petstore.swagger.io/#/).
* [Google doc](https://docs.google.com/document/d/1sjZ1RxcqU1skCoK5v7oyacerlrOChKhGQcyYA4l1cbM/edit?usp=sharing) with bug report examples.
