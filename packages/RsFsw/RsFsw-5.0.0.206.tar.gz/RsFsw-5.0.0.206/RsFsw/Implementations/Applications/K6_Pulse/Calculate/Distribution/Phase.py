from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, xaxis: enums.PulsePhaseItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:PHASe \n
		Snippet: driver.applications.k6Pulse.calculate.distribution.phase.set(xaxis = enums.PulsePhaseItems.DEViation, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display. \n
			:param xaxis: POINt | PPPHase | RERRor | PERRor | DEViation Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. POINt Pulse phase at measurement point PPPHase Pulse-Pulse Phase Difference RERRor Phase Error (RMS) PERRor Phase Error (Peak) DEViation Phase Deviation
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of pulses in which the parameter value occurred. OCCurrence Percentage of all measured pulses in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulsePhaseItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:PHASe {param}'.rstrip())
