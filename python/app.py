from flask import Flask, request
from sys import version
from austin_heller_repo.threading import Semaphore
from database import DatabaseInterface
import configparser


app = Flask(__name__)


def get_database_interface() -> DatabaseInterface:
    config = configparser.ConfigParser()
    config.read("database.ini")
    user_name = config["database"]["user_name"]
    user_password = config["database"]["user_password"]
    database_name = config["database"]["database_name"]
    return DatabaseInterface(
        connection_string=f"dbname={database_name} user={user_name} password={user_password}"
    )


@app.route("/v1/test/health", methods=["POST"])
def test_health():
    return {"healthy": True}


@app.route("/v1/api/component_manager/get_docker_api_specification", methods=["POST"])
def get_docker_api_specification():

    output = {
        "data": None,
        "exception": None
    }

    try:

        database_interface = get_database_interface()

        docker_api_specification = database_interface.get_docker_api_specification()

        output["data"] = {
            "docker_api_specification": docker_api_specification
        }

    except Exception as ex:
        output["exception"] = str(ex)

    return output


@app.route("/v1/api/component_manager/get_docker_component_specification_by_component_uuid", methods=["POST"])
def get_docker_component_specification_by_component_uuid():

    output = {
        "data": None,
        "exception": None
    }

    try:

        input_json = request.get_json()

        if "component_uuid" not in input_json:
            raise Exception(f"Failed to find \"component_uuid\" in input json \"{input_json}\".")
        else:

            component_uuid = input_json["component_uuid"]

            database_interface = get_database_interface()

            component_specification = database_interface.get_component_specification(
                component_uuid=component_uuid
            )

            output["data"] = {
                "component_specification": component_specification
            }

    except Exception as ex:
        output["exception"] = str(ex)

    return output



