import os
import requests
import sys

from dotenv import load_dotenv


def get_build_option():
    print("Build options:\n")
    print("1. Create Flask Bootstrap Infrastructure")
    print("2. Destroy Flask Bootstrap Infrastructure")
    print("3. Welcome Build")
    print("4. Exit")
    build_option = input("\nSelect build option: ")

    if build_option == "1":
        create_build(create=True, destroy=False)
    elif build_option == "2":
        create_build(create=False, destroy=True)
    elif build_option == "3":
        create_build(create=False, destroy=False)
    if build_option == "4":
        sys.exit()


def get_circle_api():
    return f"https://circleci.com/api/v2/project/github/hunt3ri/hunter-ops-launch/pipeline?circle-token={circleci_token}"


def create_build(create: bool, destroy: bool):
    print("Creating build")
    payload = {"branch": "master", "parameters": {"terraform-apply": create, "terraform-destroy": destroy}}
    response = requests.post(get_circle_api(), json=payload)

    print(f"CircleCI Response Status Code: {response.status_code}")


if __name__ == "__main__":
    load_dotenv()

    circleci_token = os.getenv("CIRCLECI_TOKEN", "NOT_SET")
    if circleci_token == "NOT_SET":
        print("ERROR: Set CIRCLECI_TOKEN in .env file")

    get_build_option()
