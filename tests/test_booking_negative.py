import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_nonexistent_booking():
    response = requests.get(f"{BASE_URL}/booking/999999")
    assert response.status_code == 404  



def test_update_booking_without_auth():
    payload = {
        "firstname": "NoAuth",
        "lastname": "Test",    
        "totalprice": 50,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-04-01",
            "checkout": "2023-04-05"
        },
        "additionalneeds": "None"
    }
    # Create a booking to update
    create_response = requests.post(f"{BASE_URL}/booking", json=payload)
    booking_id = create_response.json()["bookingid"]    

    # Attempt to update the booking without authentication
    update_response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=payload)
    assert update_response.status_code == 403  # Forbidden  
    

