from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdivision:
	"""Pdivision commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdivision", core, parent)

	def set(self, pdiv: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:PDIVision \n
		Snippet: driver.applications.k70Vsa.display.window.trace.x.scale.pdivision.set(pdiv = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the scaling of the x-axis for statistical result displays. For all other result displays, this
		command is only available as a query. \n
			:param pdiv: Defines the range per division (total range = 10*PDiv)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(pdiv)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:PDIVision {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:PDIVision \n
		Snippet: value: float = driver.applications.k70Vsa.display.window.trace.x.scale.pdivision.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the scaling of the x-axis for statistical result displays. For all other result displays, this
		command is only available as a query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: pdiv: Defines the range per division (total range = 10*PDiv)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:PDIVision?')
		return Conversions.str_to_float(response)
