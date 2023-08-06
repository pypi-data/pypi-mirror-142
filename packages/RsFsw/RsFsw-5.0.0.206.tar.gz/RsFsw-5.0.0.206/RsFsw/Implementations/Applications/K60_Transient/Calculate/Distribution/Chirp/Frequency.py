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

	def set(self, xaxis: enums.AxisFreqItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:CHIRp:FREQuency \n
		Snippet: driver.applications.k60Transient.calculate.distribution.chirp.frequency.set(xaxis = enums.AxisFreqItems.AVGFm, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display for chirp frequency parameters. \n
			:param xaxis: AVGFm | AVGNonlinear | BWIDth | CHERror | FREQuency | MAXFm | MAXNonlinear | RMSFm | RMSNonlinear CHERror Chirp state deviation FREQuency Average frequency MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation BWIDth Bandwidth AVGNonlinear Average frequency non-linearity RMSNonlinear RMS frequency non-linearity MAXNonlinear Peak frequency non-linearity
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of chirps in which the parameter value occurred. OCCurance Percentage of all measured chirps in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.AxisFreqItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:CHIRp:FREQuency {param}'.rstrip())
