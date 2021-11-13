

class DatabaseInterface():

	def __init__(self, *, connection_string: str):

		self.__connection_string = connection_string

	def get_docker_api_specification(self):
		raise NotImplementedError()

	def get_component_specification(self, *, component_uuid: str):
		raise NotImplementedError()
