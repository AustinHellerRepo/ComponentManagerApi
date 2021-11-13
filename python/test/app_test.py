import unittest
from flask import request
import app as flask_app
import json
import uuid


class AppTest(unittest.TestCase):

	def test_initialize(self):

		client = flask_app.app.test_client()

		self.assertIsNotNone(client)

	def test_health(self):

		client = flask_app.app.test_client()

		response = client.get("/v1/test/health")

		self.assertEqual(b"{\"is_healthy\":true}\n", response.data)

	def test_json_using_data(self):

		client = flask_app.app.test_client()

		input_json_bytes = b'{"hello":"world"}\n'
		input_json_string = input_json_bytes.decode()

		response = client.post("/v1/test/json/form",
			data={
				"json": input_json_string
			}
		)

		self.assertEqual(input_json_bytes, response.data)

	def test_json_using_json(self):

		client = flask_app.app.test_client()

		input_json = {"hello": "world"}

		response = client.post("/v1/test/json/json",
			json=input_json
		)

		print(f"response: {response}")

		response_json = response.json
		print(f"response_json: {response_json}")

		self.assertEqual(input_json, response_json)

	def test_json_using_json_deep(self):

		client = flask_app.app.test_client()

		input_json = {"hello": "world", "deeper": {"here": True}}

		response = client.post("/v1/test/json/json",
			json=input_json
		)

		print(f"response: {response}")

		response_json = response.json
		print(f"response_json: {response_json}")

		self.assertEqual(input_json, response_json)

	def test_get_docker_api_specification(self):

		client = flask_app.app.test_client()

		expected_response = {'data': {'docker_api_specification': {}}, 'exception': None}

		response = client.post("/v1/api/get_docker_api_specification")

		print(f"response: {response}")
		print(f"response.json: {response.json}")

		self.assertEqual(expected_response, response.json)

	def test_get_component_specification_time_delay(self):

		client = flask_app.app.test_client()

		expected_response = {'data': {'component_specification': {'git_repo_clone_url': 'https://github.com/AustinHellerRepo/TestDockerTimeDelay.git', 'is_docker_socket_needed': False, 'script_file_path': 'start.py', 'timeout_seconds': 20}}, 'exception': None}

		response = client.post("/v1/api/get_component_specification_by_component_uuid",
			json={
				"component_uuid": "f857e1c6-89e0-4b6c-bf9a-1350feba8626"
			}
		)

		print(f"response: {response}")
		print(f"response.json: {response.json}")

		self.assertEqual(expected_response, response.json)

	def test_get_component_specification_docker_spawn_script(self):

		client = flask_app.app.test_client()

		expected_response = {'data': {'component_specification': {'git_repo_clone_url': 'https://github.com/AustinHellerRepo/TestDockerSpawnScript.git', 'is_docker_socket_needed': True, 'script_file_path': 'start.py', 'timeout_seconds': 30}}, 'exception': None}

		response = client.post("/v1/api/get_component_specification_by_component_uuid",
			json={
				"component_uuid": "c5ab8136-547e-4ec1-b8f5-c5d596a04e72"
			}
		)

		print(f"response: {response}")
		print(f"response.json: {response.json}")

		self.assertEqual(expected_response, response.json)

	def test_get_component_specification_failed(self):

		client = flask_app.app.test_client()

		component_uuid = str(uuid.uuid4())

		expected_response = {
			'data': None,
			'exception': f'Failed to find component with uuid "{component_uuid}".'
		}

		response = client.post("/v1/api/get_component_specification_by_component_uuid",
			json={
				"component_uuid": component_uuid
			}
		)

		print(f"response: {response}")
		print(f"response.json: {response.json}")

		self.assertEqual(expected_response, response.json)
