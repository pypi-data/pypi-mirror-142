from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, xaxis: enums.AxisPower, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:CHIRp:POWer \n
		Snippet: driver.applications.k60Transient.calculate.distribution.chirp.power.set(xaxis = enums.AxisPower.AVGPower, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display for chirp power parameters. \n
			:param xaxis: AVGPower | MAXPower | MINPower | PWRRipple AVGPower Average power MINPower Minimum power MAXPower Maximum power PWRRipple Power ripple
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of chirps in which the parameter value occurred. OCCurance Percentage of all measured chirps in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.AxisPower), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:CHIRp:POWer {param}'.rstrip())
