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
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:PSMode[:STATe] \n
		Snippet: driver.system.communicate.rdevice.oscilloscope.psMode.state.set(state = False) \n
		Activates the use of the power splitter inserted between the 'IF 2 GHZ OUT' connector of the R&S FSW and the 'CH1' and
		'CH3' input connectors of the oscilloscope. Note that this mode requires an additional alignment with the power splitter.
		For details see 'Power splitter mode'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:PSMode:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:PSMode[:STATe] \n
		Snippet: value: bool = driver.system.communicate.rdevice.oscilloscope.psMode.state.get() \n
		Activates the use of the power splitter inserted between the 'IF 2 GHZ OUT' connector of the R&S FSW and the 'CH1' and
		'CH3' input connectors of the oscilloscope. Note that this mode requires an additional alignment with the power splitter.
		For details see 'Power splitter mode'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:PSMode:STATe?')
		return Conversions.str_to_bool(response)
