from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsedDrives:
	"""UsedDrives commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usedDrives", core, parent)

	def set(self, state: bool = None) -> None:
		"""SCPI: MMEMory:NETWork:USEDdrives \n
		Snippet: driver.massMemory.network.usedDrives.set(state = False) \n
		This command returns a list of all network drives in use. \n
			:param state: You do not have to use the parameter. If you do not include the parameter, the command returns a list of all drives in use. This is the same behavior as if you were using the parameter OFF. ON | 1 Returns a list of all drives in use including the folder information. OFF | 0 Returns a list of all drives in use.
		"""
		param = ''
		if state:
			param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:NETWork:USEDdrives {param}'.strip())

	def get(self) -> bool:
		"""SCPI: MMEMory:NETWork:USEDdrives \n
		Snippet: value: bool = driver.massMemory.network.usedDrives.get() \n
		This command returns a list of all network drives in use. \n
			:return: state: You do not have to use the parameter. If you do not include the parameter, the command returns a list of all drives in use. This is the same behavior as if you were using the parameter OFF. ON | 1 Returns a list of all drives in use including the folder information. OFF | 0 Returns a list of all drives in use."""
		response = self._core.io.query_str(f'MMEMory:NETWork:USEDdrives?')
		return Conversions.str_to_bool(response)
