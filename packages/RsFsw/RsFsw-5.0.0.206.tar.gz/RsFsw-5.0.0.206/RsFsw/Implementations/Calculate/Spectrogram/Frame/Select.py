from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, frame: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:FRAMe:SELect \n
		Snippet: driver.calculate.spectrogram.frame.select.set(frame = 1.0, window = repcap.Window.Default) \n
		This command selects a specific frame for further analysis. The command is available if no measurement is running or
		after a single sweep has ended. Note that this command is applicable for both spectrograms and PVT waterfalls. The suffix
		<n> for CALCulate determines the window and thus which display the command is applied to. \n
			:param frame: Selects a frame directly by the frame number. Valid if the time stamp is off. The range depends on the history depth. Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(frame)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:FRAMe:SELect {param}')
