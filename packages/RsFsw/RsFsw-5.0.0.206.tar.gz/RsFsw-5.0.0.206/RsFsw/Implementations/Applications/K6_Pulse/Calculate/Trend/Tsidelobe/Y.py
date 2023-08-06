from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.PulseSidelobeItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:TSIDelobe:Y \n
		Snippet: driver.applications.k6Pulse.calculate.trend.tsidelobe.y.set(yaxis = enums.PulseSidelobeItems.AMPower, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display.
		The x-axis is configured using the CALCulate<n>:TRENd:<GroupName>:X commands. This command is only available if the
		additional option R&S FSW-K6S is installed. \n
			:param yaxis: PSLevel | ISLevel | MWIDth | SDELay | CRATio | IMPower | AMPower | PCORrelation | MPHase | MFRequency Pulse parameter to be displayed on the y-axis. For a description of the available parameters see 'Time sidelobe parameters'. PSLevel peak to sidelobe level ISLevel integrated sidelobe level MWIDth mainlobe 3 dB width SDELay sidelobe delay CRATio compression ratio IMPower integrated mainlobe power AMPower average mainlobe power PCORrelation peak correlation MPHase mainlobe phase MFRequency mainlobe frequency
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.PulseSidelobeItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:TSIDelobe:Y {param}')
