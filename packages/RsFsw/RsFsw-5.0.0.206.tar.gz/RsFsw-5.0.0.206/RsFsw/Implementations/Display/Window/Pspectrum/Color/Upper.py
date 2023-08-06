from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, percentage: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PSPectrum:COLor:UPPer \n
		Snippet: driver.display.window.pspectrum.color.upper.set(percentage = 1.0, window = repcap.Window.Default) \n
		This command sets the upper percentage boundary of the persistence spectrum. \n
			:param percentage: Statistical frequency percentage. Range: 0.01 to 100, Unit: %
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(percentage)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PSPectrum:COLor:UPPer {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:PSPectrum:COLor:UPPer \n
		Snippet: value: float = driver.display.window.pspectrum.color.upper.get(window = repcap.Window.Default) \n
		This command sets the upper percentage boundary of the persistence spectrum. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: percentage: Statistical frequency percentage. Range: 0.01 to 100, Unit: %"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PSPectrum:COLor:UPPer?')
		return Conversions.str_to_float(response)
