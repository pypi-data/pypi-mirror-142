from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Copy:
	"""Copy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("copy", core, parent)

	def set(self, line: int, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:COPY \n
		Snippet: driver.applications.k30NoiseFigure.calculate.limit.copy.set(line = 1, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command copies a limit line. \n
			:param line: 1 to 8 number of the new limit line name String containing the name of the limit line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(line)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:COPY {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> int:
		"""SCPI: CALCulate<n>:LIMit<li>:COPY \n
		Snippet: value: int = driver.applications.k30NoiseFigure.calculate.limit.copy.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command copies a limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: line: 1 to 8 number of the new limit line name String containing the name of the limit line."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:COPY?')
		return Conversions.str_to_int(response)
