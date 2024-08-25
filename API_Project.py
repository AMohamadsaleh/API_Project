import requests
import json
import re


baseurl = "https://reqres.in"


def get_request():
    url = baseurl + "/api/users"

    response = requests.get(url)
    #Verfiy status code
    assert response.status_code == 200
    json_data = response.json()
    json_body = json.dumps(json_data, indent=4)
    data = json.loads(json_body)
    print(json_body)

    #Verfiy json keys
    key_data = data["data"]
    for i in key_data:
        assert len(i) == 5
        if "id" and "email" and "first_name" and "last_name" and "avatar" in i:
            print("Json keys are valid")
        else:
            print("Json keys are not valid")

    #Verfiy json values and its data type
    for j in  key_data:
        assert isinstance(j["id"] , int), "is not an integer"
        email_regx = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        avatar_regx = r'^https?://[\w.-]+/\S+\.(jpg|jpeg|png|gif|bmp)$'
        assert re.fullmatch(email_regx,j["email"]) and re.fullmatch(avatar_regx,j["avatar"])
        keys = ["email", "first_name", "last_name", "avatar"]
        for k in keys:
            assert isinstance(j[k], str), "is not s string"


def post_request():

    url = baseurl + "/api/users"

    data = {"data": [
        {

            "email": "aziz@reqres.in",
            "first_name": "aziz",
            "last_name": "mohamadsaleh",
            "avatar": "https://reqres.in/img/faces/100-image.jpg"
        }]}
    response = requests.post(url, json=data)
    #Verfiy status code
    assert response.status_code == 201
    json_data = response.json()
    key_data = data["data"][0]
    #verfiy updated data
    assert key_data["first_name"] == "aziz"
    assert key_data["last_name"] == "mohamadsaleh"
    #Verfiy email and avatar
    assert key_data["email"] == "aziz@reqres.in"
    assert key_data["avatar"] == "https://reqres.in/img/faces/100-image.jpg"
    email_regx = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    avatar_regx = r'^https?://[\w.-]+/\S+\.(jpg|jpeg|png|gif|bmp)$'
    assert re.fullmatch(email_regx, key_data["email"]) and re.fullmatch(avatar_regx, key_data["avatar"])






def put_request():
    url = baseurl + "/api/users/2"
    data = {
        "name": "Mohamad",
        "job": "Lawyer"
    }
    response = requests.put(url, json=data)
    #Verfiy status code
    assert response.status_code == 200
    json_data = response.json()
    #verfiy updated data
    assert json_data["name"] == "Mohamad"
    assert json_data["job"] == "Lawyer"

def delete_request():
    url = baseurl + "/api/users/2"
    response = requests.delete(url)
    #Verfiy status code
    assert response.status_code == 204











get_request()
post_request()
put_request()
delete_request()


