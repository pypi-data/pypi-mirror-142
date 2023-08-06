from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.PulseEmodelItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:EMODel:Y \n
		Snippet: driver.applications.k6Pulse.calculate.trend.emodel.y.set(yaxis = enums.PulseEmodelItems.FBPTime, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display.
		The x-axis is configured using the CALCulate<n>:TRENd:<GroupName>:X commands. \n
			:param yaxis: RBPTime | RLPTime | RMPTime | RHPTime | RTPTime | RLPLevel | RMPLevel | RHPLevel | RTPLevel | FBPTime | FLPTime | FMPTime | FHPTime | FTPTime | FLPLevel | FMPLevel | FHPLevel | FTPLevel RBPTime Rise Base Point Time RLPTime Rise Low Point Time RMPTime Rise Mid Point Time RHPTime Rise High Point Time RTPTime Rise Top Point Time RLPLevel Rise Low Point Level RMPLevel Rise Mid Point Level RHPLevel Rise High Point Level RTPLevel Rise Top Point Level FBPTime Fall Base Point Time FLPTime Fall Low Point Time FMPTime Fall Mid Point Time FHPTime Fall High Point Time FTPTime Fall Top Point Time FLPLevel Fall Low Point Level FMPLevel Fall Mid Point Level FHPLevel Fall High Point Level FTPLevel Fall Top Point Level
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.PulseEmodelItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:EMODel:Y {param}')
