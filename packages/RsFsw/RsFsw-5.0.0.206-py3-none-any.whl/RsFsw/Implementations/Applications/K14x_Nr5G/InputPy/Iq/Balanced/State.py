from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:IQ:BALanced[:STATe] \n
		Snippet: driver.applications.k14Xnr5G.inputPy.iq.balanced.state.set(state = False) \n
		This command defines whether the input is provided as a differential signal via all 4 Analog Baseband connectors or as a
		plain I/Q signal via 2 single-ended lines. \n
			:param state: ON | OFF | 1 | 0 ON | 1 Differential OFF | 0 Single ended
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:IQ:BALanced:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:IQ:BALanced[:STATe] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.inputPy.iq.balanced.state.get() \n
		This command defines whether the input is provided as a differential signal via all 4 Analog Baseband connectors or as a
		plain I/Q signal via 2 single-ended lines. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 Differential OFF | 0 Single ended"""
		response = self._core.io.query_str(f'INPut:IQ:BALanced:STATe?')
		return Conversions.str_to_bool(response)
