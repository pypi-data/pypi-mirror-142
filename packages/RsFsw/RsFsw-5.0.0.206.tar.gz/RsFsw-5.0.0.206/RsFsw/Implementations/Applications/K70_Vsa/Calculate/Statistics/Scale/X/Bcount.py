from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bcount:
	"""Bcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bcount", core, parent)

	def set(self, stat_nof_columns: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:BCOunt \n
		Snippet: driver.applications.k70Vsa.calculate.statistics.scale.x.bcount.set(stat_nof_columns = 1.0, window = repcap.Window.Default) \n
		This command defines the number of columns for the statistical distribution. \n
			:param stat_nof_columns: Range: 2 to 1024, Unit: none
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(stat_nof_columns)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:BCOunt {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:STATistics:SCALe:X:BCOunt \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.statistics.scale.x.bcount.get(window = repcap.Window.Default) \n
		This command defines the number of columns for the statistical distribution. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: stat_nof_columns: Range: 2 to 1024, Unit: none"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:SCALe:X:BCOunt?')
		return Conversions.str_to_float(response)
