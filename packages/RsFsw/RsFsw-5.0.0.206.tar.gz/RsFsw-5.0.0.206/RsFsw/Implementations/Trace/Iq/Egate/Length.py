from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, gate_length: float) -> None:
		"""SCPI: TRACe:IQ:EGATe:LENGth \n
		Snippet: driver.trace.iq.egate.length.set(gate_length = 1.0) \n
		This command defines the gate length for gated measurements with the I/Q analyzer. Defines the gate length in samples in
		edge mode. For details see 'Configuring I/Q gating'. \n
			:param gate_length: numeric value Max = (440 MS * sample rate/200MHz) -1 pretrigger samples defined by TRACe:IQ:SET; sample rate defined by method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) Range: 1…Max (samples)
		"""
		param = Conversions.decimal_value_to_str(gate_length)
		self._core.io.write(f'TRACe:IQ:EGATe:LENGth {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:EGATe:LENGth \n
		Snippet: value: float = driver.trace.iq.egate.length.get() \n
		This command defines the gate length for gated measurements with the I/Q analyzer. Defines the gate length in samples in
		edge mode. For details see 'Configuring I/Q gating'. \n
			:return: gate_length: numeric value Max = (440 MS * sample rate/200MHz) -1 pretrigger samples defined by TRACe:IQ:SET; sample rate defined by method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_) Range: 1…Max (samples)"""
		response = self._core.io.query_str(f'TRACe:IQ:EGATe:LENGth?')
		return Conversions.str_to_float(response)
