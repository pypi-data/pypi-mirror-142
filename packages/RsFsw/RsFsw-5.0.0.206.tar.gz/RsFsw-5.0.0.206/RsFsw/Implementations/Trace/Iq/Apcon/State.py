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
		"""SCPI: TRACe:IQ:APCon[:STATe] \n
		Snippet: driver.trace.iq.apcon.state.set(state = False) \n
		If enabled, the average power consumption is calculated at the end of the I/Q data measurement. This command must be set
		before the measurement is performed! The conversion factors A and B for the calculation are defined using method RsFsw.
		Trace.Iq.Apcon.A.set and method RsFsw.Trace.Iq.Apcon.B.set. The results can be queried using method RsFsw.Trace.Iq.Apcon.
		Result.get_. For details see 'Average power consumption'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:APCon:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:APCon[:STATe] \n
		Snippet: value: bool = driver.trace.iq.apcon.state.get() \n
		If enabled, the average power consumption is calculated at the end of the I/Q data measurement. This command must be set
		before the measurement is performed! The conversion factors A and B for the calculation are defined using method RsFsw.
		Trace.Iq.Apcon.A.set and method RsFsw.Trace.Iq.Apcon.B.set. The results can be queried using method RsFsw.Trace.Iq.Apcon.
		Result.get_. For details see 'Average power consumption'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:APCon:STATe?')
		return Conversions.str_to_bool(response)
