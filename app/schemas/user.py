def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "firstName": item["firstName"],
        "lastName": item["lastName"],
        "password": item["password"],
    }


def usersEntity(array) -> list:
    return [userEntity(item) for item in array]
