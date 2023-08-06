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

	def set(self, yaxis: enums.AxisPower, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:CHIRp:POWer:Y \n
		Snippet: driver.applications.k60Transient.calculate.trend.chirp.power.y.set(yaxis = enums.AxisPower.AVGPower, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display for chirp power parameters. \n
			:param yaxis: AVGPower | MAXPower | MINPower | PWRRipple AVGPower Average power MINPower Minimum power MAXPower Maximum power PWRRipple Power ripple
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.AxisPower)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:CHIRp:POWer:Y {param}')
