import psycopg2


class DatabaseInterface():

	def __init__(self, *, connection_string: str):

		self.__connection_string = connection_string

	def get_docker_api_specification(self):
		# TODO implement
		return {}

	def get_component_specification(self, *, component_uuid: str):
		# TODO implement
		if component_uuid == "f857e1c6-89e0-4b6c-bf9a-1350feba8626":
			# time delay
			return {
				"git_repo_clone_url": "https://github.com/AustinHellerRepo/TestDockerTimeDelay.git",
				"script_file_path": "start.py",
				"timeout_seconds": 20,
				"is_docker_socket_needed": False
			}
		elif component_uuid == "c5ab8136-547e-4ec1-b8f5-c5d596a04e72":
			# docker spawn script
			return {
				"git_repo_clone_url": "https://github.com/AustinHellerRepo/TestDockerSpawnScript.git",
				"script_file_path": "start.py",
				"timeout_seconds": 30,
				"is_docker_socket_needed": True
			}
		else:
			raise Exception(f"Failed to find component with uuid \"{component_uuid}\".")
