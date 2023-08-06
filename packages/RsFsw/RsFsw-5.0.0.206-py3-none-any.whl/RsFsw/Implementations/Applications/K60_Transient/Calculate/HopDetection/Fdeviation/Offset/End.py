from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class End:
	"""End commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("end", core, parent)

	def set(self, time: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:FDEViation:OFFSet:END \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.fdeviation.offset.end.set(time = 1.0, window = repcap.Window.Default) \n
		Defines the end of the measurement range for frequency deviation results as an offset in seconds from the hop end. This
		command is only available if the reference is EDGE (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.
		Fdeviation.Reference.set) . For details on the measurement range parameters see 'Measurement range'. \n
			:param time: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:FDEViation:OFFSet:END {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:HOPDetection:FDEViation:OFFSet:END \n
		Snippet: value: float = driver.applications.k60Transient.calculate.hopDetection.fdeviation.offset.end.get(window = repcap.Window.Default) \n
		Defines the end of the measurement range for frequency deviation results as an offset in seconds from the hop end. This
		command is only available if the reference is EDGE (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.
		Fdeviation.Reference.set) . For details on the measurement range parameters see 'Measurement range'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: time: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:FDEViation:OFFSet:END?')
		return Conversions.str_to_float(response)
