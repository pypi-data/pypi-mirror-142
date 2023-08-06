from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.LoadType) -> None:
		"""SCPI: MMEMory:LOAD:TYPE \n
		Snippet: driver.massMemory.load.typePy.set(type_py = enums.LoadType.NEW) \n
		This command defines whether the channels that will be loaded with the subsequent method RsFsw.MassMemory.Load.State.set
		command will replace the current channel or activate a new channel. \n
			:param type_py: NEW | REPLace NEW The loaded settings will be activated in a new channel. REPLace The loaded settings will replace the currently active channel.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.LoadType)
		self._core.io.write(f'MMEMory:LOAD:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LoadType:
		"""SCPI: MMEMory:LOAD:TYPE \n
		Snippet: value: enums.LoadType = driver.massMemory.load.typePy.get() \n
		This command defines whether the channels that will be loaded with the subsequent method RsFsw.MassMemory.Load.State.set
		command will replace the current channel or activate a new channel. \n
			:return: type_py: NEW | REPLace NEW The loaded settings will be activated in a new channel. REPLace The loaded settings will replace the currently active channel."""
		response = self._core.io.query_str(f'MMEMory:LOAD:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.LoadType)
