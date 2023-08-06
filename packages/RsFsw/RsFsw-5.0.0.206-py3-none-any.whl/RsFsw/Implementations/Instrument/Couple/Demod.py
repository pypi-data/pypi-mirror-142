from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	def set(self, state: enums.Synchronization) -> None:
		"""SCPI: INSTrument:COUPle:DEMod \n
		Snippet: driver.instrument.couple.demod.set(state = enums.Synchronization.ALL) \n
		This command turns synchronization of the audio demodulator configuration between measurement channels on and off. \n
			:param state: ALL | NONE ALL Turns on synchronization. NONE Turns off synchronization.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.Synchronization)
		self._core.io.write(f'INSTrument:COUPle:DEMod {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Synchronization:
		"""SCPI: INSTrument:COUPle:DEMod \n
		Snippet: value: enums.Synchronization = driver.instrument.couple.demod.get() \n
		This command turns synchronization of the audio demodulator configuration between measurement channels on and off. \n
			:return: state: ALL | NONE ALL Turns on synchronization. NONE Turns off synchronization."""
		response = self._core.io.query_str(f'INSTrument:COUPle:DEMod?')
		return Conversions.str_to_scalar_enum(response, enums.Synchronization)
