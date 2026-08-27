API Testing Automation

Automated API testing suite built with Python, pytest, and requests, covering full CRUD operations and negative/security test cases against the Restful-booker public API.

What this project demonstrates
Full CRUD test coverage (Create, Read, Update, Delete)
Authentication handling (token-based login)
Negative testing: invalid resources, missing authentication
Clear separation between positive and negative test suites
Response validation: status codes and response body assertions
Project structure
api-testing-automation/
├── tests/
│   ├── test_bookings_positive.py   # CRUD happy-path tests
│   └── test_bookings_negative.py   # Negative / security test cases
├── requirements.txt
└── README.md
Tests overview

Positive tests (test_bookings_positive.py)

test_get_all_bookings — retrieves the list of bookings
test_create_booking — creates a new booking and validates the response
test_update_booking — authenticates and updates an existing booking
test_delete_booking — authenticates, deletes a booking, and confirms it no longer exists

Negative tests (test_bookings_negative.py)

test_get_nonexistent_booking — verifies a proper 404 for a non-existent resource
test_update_booking_without_auth — verifies the API rejects updates without an authentication token (403)