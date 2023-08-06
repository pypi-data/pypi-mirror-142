from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: OUTPut:DIQ[:STATe] \n
		Snippet: driver.output.diq.state.set(state = False) \n
		This command turns continuous output of I/Q data to the optional Digital Baseband Interface on and off. Using the digital
		input and digital output simultaneously is not possible. If digital baseband output is active, the sample rate is
		restricted to 100 MHz (200 MHz if enhanced mode is possible; max. 160 MHz bandwidth) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut:DIQ:STATe {param}')

	def get(self) -> bool:
		"""SCPI: OUTPut:DIQ[:STATe] \n
		Snippet: value: bool = driver.output.diq.state.get() \n
		This command turns continuous output of I/Q data to the optional Digital Baseband Interface on and off. Using the digital
		input and digital output simultaneously is not possible. If digital baseband output is active, the sample rate is
		restricted to 100 MHz (200 MHz if enhanced mode is possible; max. 160 MHz bandwidth) . \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'OUTPut:DIQ:STATe?')
		return Conversions.str_to_bool(response)
