from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, statistic_mode: enums.StatisticMode, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:MODE \n
		Snippet: driver.applications.k70Vsa.calculate.statistics.mode.set(statistic_mode = enums.StatisticMode.INFinite, window = repcap.Window.Default) \n
		This command defines whether only the symbol points or all points are considered for the statistical calculations. \n
			:param statistic_mode: SONLy | INFinite SONLy Symbol points only are used INFinite All points are used
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(statistic_mode, enums.StatisticMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.StatisticMode:
		"""SCPI: CALCulate<n>:STATistics:MODE \n
		Snippet: value: enums.StatisticMode = driver.applications.k70Vsa.calculate.statistics.mode.get(window = repcap.Window.Default) \n
		This command defines whether only the symbol points or all points are considered for the statistical calculations. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: statistic_mode: SONLy | INFinite SONLy Symbol points only are used INFinite All points are used"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.StatisticMode)
