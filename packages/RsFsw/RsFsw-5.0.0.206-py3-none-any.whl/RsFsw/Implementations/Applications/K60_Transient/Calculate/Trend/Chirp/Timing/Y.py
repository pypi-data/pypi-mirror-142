from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.AxisTimingItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:CHIRp:TIMing:Y \n
		Snippet: driver.applications.k60Transient.calculate.trend.chirp.timing.y.set(yaxis = enums.AxisTimingItems.BEGin, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display for chirp timing parameters. \n
			:param yaxis: BEGin | LENGth | RATE BEGin Chirp Begin LENGth Chirp length RATe Chirp rate
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.AxisTimingItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:CHIRp:TIMing:Y {param}')
