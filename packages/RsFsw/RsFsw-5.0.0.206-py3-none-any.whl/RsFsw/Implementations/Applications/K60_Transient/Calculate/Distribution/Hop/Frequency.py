from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, xaxis: enums.AxisFreqFmItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:HOP:FREQuency \n
		Snippet: driver.applications.k60Transient.calculate.distribution.hop.frequency.set(xaxis = enums.AxisFreqFmItems.AVGFm, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display for hop frequency parameters. \n
			:param xaxis: AVGFm | FMERror | FREQuency | MAXFm | RELFrequency | RMSFm FREQuency Average frequency RELFrequency Relative frequency (hop-to-hop) FMERror Hop state deviation MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of hops in which the parameter value occurred. OCCurance Percentage of all measured hops in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.AxisFreqFmItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:HOP:FREQuency {param}'.rstrip())
