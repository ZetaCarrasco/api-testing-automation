# API Testing Automation

Automated API testing suite built with Python, pytest, and requests, covering full CRUD operations and negative test cases (non-existent resources, missing authentication) against the Restful-booker public API.

The tests run against [Restful-booker](https://restful-booker.herokuapp.com), a public practice API. Since the API is shared and cannot be reset, each test creates its own data instead of relying on existing records.

## What this project demonstrates

- Full CRUD test coverage (Create, Read, Update, Delete)
- Authentication handling (token-based login)
- Negative testing: invalid resources, missing authentication
- Clear separation between positive and negative test suites
- Response validation: status codes and response body assertions

## Project structure

```
api-testing-automation/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI: runs the tests on every push and pull request
├── tests/
│   ├── test_booking_positive.py   # CRUD happy-path tests
│   └── test_booking_negative.py   # Negative test cases
├── requirements.txt
└── README.md
```

## Tests overview

### Positive tests (`test_booking_positive.py`)

- `test_get_all_bookings` — retrieves the list of bookings
- `test_create_booking` — creates a new booking and validates the response
- `test_update_booking` — authenticates and updates an existing booking
- `test_delete_booking` — authenticates, deletes a booking, and confirms it no longer exists

### Negative tests (`test_booking_negative.py`)

- `test_get_nonexistent_booking` — verifies a proper 404 for a non-existent resource
- `test_update_booking_without_auth` — verifies the API rejects updates without an authentication token (403)

## Getting started

Requires Python 3.12 (the version used in CI).

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Continuous integration

A GitHub Actions workflow runs the full test suite on every push and pull request: it sets up Python 3.12, installs the dependencies from `requirements.txt`, and runs `pytest`.