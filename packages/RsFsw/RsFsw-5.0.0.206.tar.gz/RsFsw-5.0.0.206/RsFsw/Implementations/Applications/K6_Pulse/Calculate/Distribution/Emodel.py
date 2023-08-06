from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emodel:
	"""Emodel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emodel", core, parent)

	def set(self, xaxis: enums.PulseEmodelItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:EMODel \n
		Snippet: driver.applications.k6Pulse.calculate.distribution.emodel.set(xaxis = enums.PulseEmodelItems.FBPTime, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display. \n
			:param xaxis: RBPTime | RLPTime | RMPTime | RHPTime | RTPTime | RLPLevel | RMPLevel | RHPLevel | RTPLevel | FBPTime | FLPTime | FMPTime | FHPTime | FTPTime | FLPLevel | FMPLevel | FHPLevel | FTPLevel RBPTime Rise Base Point Time RLPTime Rise Low Point Time RMPTime Rise Mid Point Time RHPTime Rise High Point Time RTPTime Rise Top Point Time RLPLevel Rise Low Point Level RMPLevel Rise Mid Point Level RHPLevel Rise High Point Level RTPLevel Rise Top Point Level FBPTime Fall Base Point Time FLPTime Fall Low Point Time FMPTime Fall Mid Point Time FHPTime Fall High Point Time FTPTime Fall Top Point Time FLPLevel Fall Low Point Level FMPLevel Fall Mid Point Level FHPLevel Fall High Point Level FTPLevel Fall Top Point Level
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of pulses in which the parameter value occurred. OCCurrence Percentage of all measured pulses in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulseEmodelItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:EMODel {param}'.rstrip())
