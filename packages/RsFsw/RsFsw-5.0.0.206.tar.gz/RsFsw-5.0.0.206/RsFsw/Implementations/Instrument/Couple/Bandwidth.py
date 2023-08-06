from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, state: enums.Synchronization) -> None:
		"""SCPI: INSTrument:COUPle:BWIDth \n
		Snippet: driver.instrument.couple.bandwidth.set(state = enums.Synchronization.ALL) \n
		This command turns synchronization of the resolution bandwidth (and filter type) between measurement channels on and off. \n
			:param state: ALL | NONE ALL Turns on synchronization. NONE Turns on synchronization.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.Synchronization)
		self._core.io.write(f'INSTrument:COUPle:BWIDth {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Synchronization:
		"""SCPI: INSTrument:COUPle:BWIDth \n
		Snippet: value: enums.Synchronization = driver.instrument.couple.bandwidth.get() \n
		This command turns synchronization of the resolution bandwidth (and filter type) between measurement channels on and off. \n
			:return: state: ALL | NONE ALL Turns on synchronization. NONE Turns on synchronization."""
		response = self._core.io.query_str(f'INSTrument:COUPle:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.Synchronization)
