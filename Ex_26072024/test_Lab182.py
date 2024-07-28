import pytest
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amit",
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
    print(type(URL))
    print(type(headers))
    print(type(payload))

    # Assertions
    assert response.status_code == 200
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_update_req_1(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    payload = {
        "firstname": "Vimal",
        "lastname": "Patel",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Vimal"
    assert data["lastname"] == "Patel"


def test_update_req_2(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    payload = {
        "firstname": "Vimal",
        "lastname": "Patel",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Vimal"
    assert data["lastname"] == "Patel"