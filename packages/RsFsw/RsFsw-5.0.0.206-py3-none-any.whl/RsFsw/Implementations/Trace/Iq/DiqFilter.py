from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DiqFilter:
	"""DiqFilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diqFilter", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ:DIQFilter \n
		Snippet: driver.trace.iq.diqFilter.set(state = False) \n
		This command is only available when using the optional Digital Baseband Interface. By default, a decimation filter is
		used during data acquisition to reduce the sample rate to the value defined using method RsFsw.Applications.K10x_Lte.
		Trace.Iq.SymbolRate.get_. If the filter is bypassed, the sample rate is identical to the input sample rate configured for
		the Digital I/Q input source (see method RsFsw.Applications.K10x_Lte.InputPy.Diq.SymbolRate.set) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:DIQFilter {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ:DIQFilter \n
		Snippet: value: bool = driver.trace.iq.diqFilter.get() \n
		This command is only available when using the optional Digital Baseband Interface. By default, a decimation filter is
		used during data acquisition to reduce the sample rate to the value defined using method RsFsw.Applications.K10x_Lte.
		Trace.Iq.SymbolRate.get_. If the filter is bypassed, the sample rate is identical to the input sample rate configured for
		the Digital I/Q input source (see method RsFsw.Applications.K10x_Lte.InputPy.Diq.SymbolRate.set) . \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:DIQFilter?')
		return Conversions.str_to_bool(response)
