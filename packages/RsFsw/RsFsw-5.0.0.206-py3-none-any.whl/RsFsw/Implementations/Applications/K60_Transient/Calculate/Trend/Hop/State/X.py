from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, xaxis: enums.AxisHopState, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:STATe:X \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.state.x.set(xaxis = enums.AxisHopState.INDex, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display for hop state parameters. \n
			:param xaxis: INDex | STAFrequency INDex Hop index STAFrequency State frequency (nominal)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.AxisHopState)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:STATe:X {param}')
