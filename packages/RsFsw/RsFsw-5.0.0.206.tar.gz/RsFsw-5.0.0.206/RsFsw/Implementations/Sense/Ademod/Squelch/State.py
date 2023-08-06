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
		"""SCPI: [SENSe]:ADEMod:SQUelch[:STATe] \n
		Snippet: driver.sense.ademod.squelch.state.set(state = False) \n
		This command activates the squelch function, i.e. if the signal falls below a defined threshold (see
		[SENSe:]ADEMod:SQUelch:LEVel) , the demodulated data is automatically set to 0. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:SQUelch:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod:SQUelch[:STATe] \n
		Snippet: value: bool = driver.sense.ademod.squelch.state.get() \n
		This command activates the squelch function, i.e. if the signal falls below a defined threshold (see
		[SENSe:]ADEMod:SQUelch:LEVel) , the demodulated data is automatically set to 0. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SQUelch:STATe?')
		return Conversions.str_to_bool(response)
