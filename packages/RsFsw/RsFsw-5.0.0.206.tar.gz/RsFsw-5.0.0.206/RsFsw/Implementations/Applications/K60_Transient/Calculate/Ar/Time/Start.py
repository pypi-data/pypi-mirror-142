from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, start_time: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:AR:TIME:STARt \n
		Snippet: driver.applications.k60Transient.calculate.ar.time.start.set(start_time = 1.0, window = repcap.Window.Default) \n
		Defines the starting point of the time span for the analysis region. The starting point is defined as a time offset from
		the capture start time. \n
			:param start_time: Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(start_time)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:AR:TIME:STARt {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:AR:TIME:STARt \n
		Snippet: value: float = driver.applications.k60Transient.calculate.ar.time.start.get(window = repcap.Window.Default) \n
		Defines the starting point of the time span for the analysis region. The starting point is defined as a time offset from
		the capture start time. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: start_time: Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:AR:TIME:STARt?')
		return Conversions.str_to_float(response)
