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

	def set(self, yaxis: enums.AxisFmSettling, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:FMSettling:Y \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.fmSettling.y.set(yaxis = enums.AxisFmSettling.FMSLength, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display for hop FM settling parameters. \n
			:param yaxis: FMSLength | FMSPoint | FMSTime FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.AxisFmSettling)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:FMSettling:Y {param}')
