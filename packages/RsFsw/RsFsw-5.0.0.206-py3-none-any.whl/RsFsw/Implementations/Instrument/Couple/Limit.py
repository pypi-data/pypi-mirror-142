from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def set(self, state: enums.Synchronization) -> None:
		"""SCPI: INSTrument:COUPle:LIMit \n
		Snippet: driver.instrument.couple.limit.set(state = enums.Synchronization.ALL) \n
		This command turns synchronization of limit results between measurement channels on and off. \n
			:param state: ALL | NONE ALL Turns on synchronization. Limit lines have to be compatible to the x-axis and y-axis configuration for successful synchronization. NONE Turns off synchronization.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.Synchronization)
		self._core.io.write(f'INSTrument:COUPle:LIMit {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Synchronization:
		"""SCPI: INSTrument:COUPle:LIMit \n
		Snippet: value: enums.Synchronization = driver.instrument.couple.limit.get() \n
		This command turns synchronization of limit results between measurement channels on and off. \n
			:return: state: ALL | NONE ALL Turns on synchronization. Limit lines have to be compatible to the x-axis and y-axis configuration for successful synchronization. NONE Turns off synchronization."""
		response = self._core.io.query_str(f'INSTrument:COUPle:LIMit?')
		return Conversions.str_to_scalar_enum(response, enums.Synchronization)
