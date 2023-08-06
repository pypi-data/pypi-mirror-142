from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:SQUelch[:STATe] \n
		Snippet: driver.sense.demod.squelch.state.set(state = False) \n
		This command turns selective demodulation at the marker position on and off. For selective demodulation, the R&S FSW
		turns on a video trigger whose level correponds to the squelch level. Therefore it turns other triggers or gates off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:SQUelch:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:SQUelch[:STATe] \n
		Snippet: value: bool = driver.sense.demod.squelch.state.get() \n
		This command turns selective demodulation at the marker position on and off. For selective demodulation, the R&S FSW
		turns on a video trigger whose level correponds to the squelch level. Therefore it turns other triggers or gates off. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DEMod:SQUelch:STATe?')
		return Conversions.str_to_bool(response)
