from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)

	def set(self, samples: float) -> None:
		"""SCPI: TRACe:IQ:EGATe:GAP \n
		Snippet: driver.trace.iq.egate.gap.set(samples = 1.0) \n
		This command defines the interval between several gate periods for gated measurements with the I/Q analyzer. \n
			:param samples: numeric value Max = (440 MS * sample rate/200MHz) -1 pretrigger samples defined by TRACe:IQ:SET; sample rate defined by method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) Range: 1…Max (samples)
		"""
		param = Conversions.decimal_value_to_str(samples)
		self._core.io.write(f'TRACe:IQ:EGATe:GAP {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:EGATe:GAP \n
		Snippet: value: float = driver.trace.iq.egate.gap.get() \n
		This command defines the interval between several gate periods for gated measurements with the I/Q analyzer. \n
			:return: samples: numeric value Max = (440 MS * sample rate/200MHz) -1 pretrigger samples defined by TRACe:IQ:SET; sample rate defined by method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) Range: 1…Max (samples)"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:GAP?')
		return Conversions.str_to_float(response)
