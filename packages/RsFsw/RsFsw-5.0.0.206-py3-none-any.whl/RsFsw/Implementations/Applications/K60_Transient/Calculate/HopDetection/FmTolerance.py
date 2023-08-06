from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmTolerance:
	"""FmTolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmTolerance", core, parent)

	def set(self, tolerance: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:FMTolerance \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.fmTolerance.set(tolerance = 1.0, window = repcap.Window.Default) \n
		Defines the allowed deviation from the detected FM signal model state where the hop is considered as 'settled'. \n
			:param tolerance: Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:FMTolerance {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:HOPDetection:FMTolerance \n
		Snippet: value: float = driver.applications.k60Transient.calculate.hopDetection.fmTolerance.get(window = repcap.Window.Default) \n
		Defines the allowed deviation from the detected FM signal model state where the hop is considered as 'settled'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: tolerance: Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:FMTolerance?')
		return Conversions.str_to_float(response)
