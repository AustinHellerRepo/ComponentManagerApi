from flask import Flask, request
from sys import version
from austin_heller_repo.threading import Semaphore
from database import DatabaseInterface


app = Flask(__name__)


@app.route("/v1/test/health", methods=["POST"])
def test_health():
    return {"healthy": True}


@app.route("/v1/api/component_manager/get_docker_api_specification", methods=["POST"])
def get_docker_api_specification():

    database_interface = DatabaseInterface(
        connection_string=
    )


@app.route("/v1/api/component_manager/get_docker_component_specification_by_component_uuid", methods=["POST"])
def get_docker_component_specification_by_component_uuid():
    raise NotImplementedError()



