from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Feed:
	"""Feed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("feed", core, parent)

	def set(self, window_type: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: driver.applications.k17Mcgd.calculate.feed.set(window_type = '1', window = repcap.Window.Default) \n
		This command selects the evaluation method of the measured data that is to be displayed in the specified window.
		This command queries or sets the diagram type (for magnitude or for phase) . Note that this command is maintained for
		compatibility reasons only. Use the LAYout commands for new remote control programs (see 'Working with windows in the
		display') . \n
			:param window_type: 'XFRequency:SPECtrum[:MAGNitude]' Magnitude diagram 'XFRequency:SPECtrum:PHASe' Phase diagram
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(window_type)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FEED {param}')
