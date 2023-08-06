from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, xaxis: enums.AxisPhase, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:CHIRp:PHASe \n
		Snippet: driver.applications.k60Transient.calculate.distribution.chirp.phase.set(xaxis = enums.AxisPhase.AVPHm, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the x-axis and y-axis of the Parameter Distribution result display for chirp phase parameters over time. \n
			:param xaxis: AVPHm | MXPHm | RMSPm AVPHm Average phase deviation MXPHm Maximum phase deviation RMSPm RMS phase deviation
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of hops in which the parameter value occurred. OCCurance Percentage of all measured hops in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.AxisPhase), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:CHIRp:PHASe {param}'.rstrip())
