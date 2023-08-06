from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmSettling:
	"""FmSettling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmSettling", core, parent)

	def set(self, xaxis: enums.AxisFmSettling, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:HOP:FMSettling \n
		Snippet: driver.applications.k60Transient.calculate.distribution.hop.fmSettling.set(xaxis = enums.AxisFmSettling.FMSLength, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display for hop FM settling parameters. \n
			:param xaxis: FMSLength | FMSPoint | FMSTime FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of hops in which the parameter value occurred. OCCurance Percentage of all measured hops in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.AxisFmSettling), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:HOP:FMSettling {param}'.rstrip())
