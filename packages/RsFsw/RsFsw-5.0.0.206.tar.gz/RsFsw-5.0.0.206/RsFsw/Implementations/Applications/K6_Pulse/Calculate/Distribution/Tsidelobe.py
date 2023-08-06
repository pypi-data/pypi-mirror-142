from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsidelobe:
	"""Tsidelobe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsidelobe", core, parent)

	def set(self, xaxis: enums.PulseSidelobeItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:TSIDelobe \n
		Snippet: driver.applications.k6Pulse.calculate.distribution.tsidelobe.set(xaxis = enums.PulseSidelobeItems.AMPower, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Time Sidelobe Parameter Distribution result display. This command is only available if the additional
		option R&S FSW-K6S is installed. \n
			:param xaxis: PSLevel | ISLevel | MWIDth | SDELay | CRATio | IMPower | AMPower | PCORrelation | MPHase | MFRequency Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Time sidelobe parameters'. PSLevel peak to sidelobe level ISLevel integrated sidelobe level MWIDth mainlobe 3 dB width SDELay sidelobe delay CRATio compression ratio IMPower integrated mainlobe power AMPower average mainlobe power PCORrelation peak correlation MPHase mainlobe phase MFRequency mainlobe frequency
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of pulses in which the parameter value occurred. OCCurrence Percentage of all measured pulses in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulseSidelobeItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:TSIDelobe {param}'.rstrip())
