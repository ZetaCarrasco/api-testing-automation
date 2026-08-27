import requests

BASE_URL= "https://restful-booker.herokuapp.com"

def test_get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_creat_booking():
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == payload["firstname"]
    assert response.json()["booking"]["lastname"] == payload["lastname"]    

def test_update_booking():
    #Firts, create a booking to update
    payload = {
        "firstname": "Maria",
        "lastname": "Lopez",  
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-02-01",
            "checkout": "2023-02-10"
        },
        "additionalneeds": "Lunch"
    }
    create_response = requests.post(f"{BASE_URL}/booking", json=payload)
    booking_id = create_response.json()["bookingid"]

    # Now, update the booking
    update_payload = {
        "username": "admin",
        "password": "password123",
    }
    auth_response = requests.post(f"{BASE_URL}/auth", json=update_payload)
    token = auth_response.json()["token"]

    # Update the booking with new data
    update_payload = payload.copy()
    update_payload["firstname"] = "MariaUpdated"

    headres = {"Cookie": f"token={token}"}
    update_response = requests.put(
        f"{BASE_URL}/booking/{booking_id}", 
        json=update_payload,
        headers=headres)

    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == "MariaUpdated"


def test_delete_booking():
    # First, create a booking to delete
    payload = {
        "firstname": "Carlos",
        "lastname": "Ruiz",
        "totalprice": 100,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-03-01",
            "checkout": "2023-03-05"
        },
        "additionalneeds": "Dinner"
    }
    create_response = requests.post(f"{BASE_URL}/booking", json=payload)
    booking_id = create_response.json()["bookingid"]

    # Authenticate to get the token
    auth_payload = {
        "username": "admin",
        "password": "password123",
    }
    auth_response = requests.post(f"{BASE_URL}/auth", json=auth_payload)
    token = auth_response.json()["token"]

    # Delete the booking
    headers = {"Cookie": f"token={token}"}
    delete_response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)

    assert delete_response.status_code == 201

    # Verify that the booking has been deleted
    get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert get_response.status_code == 404    


