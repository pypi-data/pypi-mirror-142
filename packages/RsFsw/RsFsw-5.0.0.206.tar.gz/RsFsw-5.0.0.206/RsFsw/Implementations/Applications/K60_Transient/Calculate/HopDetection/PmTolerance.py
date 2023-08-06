from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmTolerance:
	"""PmTolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmTolerance", core, parent)

	def set(self, tolerance: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:PMTolerance \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.pmTolerance.set(tolerance = 1.0, window = repcap.Window.Default) \n
		Defines the allowed deviation from the detected PM signal model state where the hop is considered as 'settled'. \n
			:param tolerance: Unit: degrees
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:PMTolerance {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:HOPDetection:PMTolerance \n
		Snippet: value: float = driver.applications.k60Transient.calculate.hopDetection.pmTolerance.get(window = repcap.Window.Default) \n
		Defines the allowed deviation from the detected PM signal model state where the hop is considered as 'settled'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: tolerance: Unit: degrees"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:PMTolerance?')
		return Conversions.str_to_float(response)
