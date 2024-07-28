import allure
import pytest
import requests


@pytest.fixture()
@allure.title("Create a new booking")
def create_booking():
    print("Create Booking ID")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    return booking_id


@allure.title("#TC2 - Delete the booking and Verify that it should not exist")
@pytest.mark.integration
def test_create_and_delete_booking(create_booking, create_token):
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking

    # Delete the booking
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }

    delete_response = requests.delete(url=DELETE_URL, headers=headers)
    assert delete_response.status_code == 201
    print(f"Deleted Booking ID: {booking_id}")

    # Verify booking should not exist after deletion
    get_response = requests.get(url=DELETE_URL)
    assert get_response.status_code == 404
    print(f"Verified Booking ID {booking_id} does not exist")
