from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stability:
	"""Stability commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stability", core, parent)

	def set(self, yaxis: enums.PulseYaxisItem, xaxis: enums.PulseAxisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:STABility \n
		Snippet: driver.applications.k6Pulse.calculate.trend.stability.set(yaxis = enums.PulseYaxisItem.AMPLitude, xaxis = enums.PulseAxisItems.DCYCle, window = repcap.Window.Default) \n
		No command help available \n
			:param yaxis: No help available
			:param xaxis: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('yaxis', yaxis, DataType.Enum, enums.PulseYaxisItem), ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulseAxisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:STABility {param}'.rstrip())
