import pytest
import requests


@pytest.fixture()
def create_token():
    # Token
    print("Create Token")
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
    print("Create Booking ID")
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


@pytest.fixture
def read_csv_file_data():
    pass


@pytest.fixture
def read_mysql_file_database():
    pass


@pytest.fixture
def launch_browser():
    print("Launching a Browser!! Chrome")
    return "chrome"


@pytest.fixture
def close_browser():
    print("Closing a Browser!! Chrome")
    return "closed"


@pytest.fixture
def read_url_testdata_excel():
    pass
