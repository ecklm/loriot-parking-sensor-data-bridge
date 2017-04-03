from sensor_model import sensormessage

class Poller:
	def connect(self) -> None:
		pass

	def close(self) -> None:
		"""
		Closes
		:return: 
		"""
		pass

	def isConnected(self) -> bool:
		"""
		
		:return: Whether the poller is connected to its' source or not. 
		"""
		pass

	def recv(self) -> sensormessage.SensorMessage or None:
		"""

		:return: 
		"""
		pass

	def __json2loriotMessage(self, inbound_message) -> sensormessage.SensorMessage or dict:
		"""

		:param dict inbound_message: The dict decoded from json.
		:return: A message object with the required fields.
			If the inbound JS object is not like what we need, it only returns the original python object
		"""
		pass
