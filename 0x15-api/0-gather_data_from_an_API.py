#!usr/bin/python3
"""Python script that Returns information about an
employees TODO list progress for a given ID
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    complete = [t.get("title") for t in to_do if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(complete), len(to_do)))
    [print("\t {}".format(c)) for c in complete]
