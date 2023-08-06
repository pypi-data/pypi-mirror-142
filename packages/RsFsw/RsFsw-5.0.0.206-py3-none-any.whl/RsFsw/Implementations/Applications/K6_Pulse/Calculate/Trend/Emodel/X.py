from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, xaxis: enums.PulseEmodelItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:EMODel:X \n
		Snippet: driver.applications.k6Pulse.calculate.trend.emodel.x.set(xaxis = enums.PulseEmodelItems.FBPTime, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display.
		The y-axis is configured using the CALCulate<n>:TRENd:<GroupName>:Y commands. \n
			:param xaxis: RBPTime | RLPTime | RMPTime | RHPTime | RTPTime | RLPLevel | RMPLevel | RHPLevel | RTPLevel | FBPTime | FLPTime | FMPTime | FHPTime | FTPTime | FLPLevel | FMPLevel | FHPLevel | FTPLevel RBPTime Rise Base Point Time RLPTime Rise Low Point Time RMPTime Rise Mid Point Time RHPTime Rise High Point Time RTPTime Rise Top Point Time RLPLevel Rise Low Point Level RMPLevel Rise Mid Point Level RHPLevel Rise High Point Level RTPLevel Rise Top Point Level FBPTime Fall Base Point Time FLPTime Fall Low Point Time FMPTime Fall Mid Point Time FHPTime Fall High Point Time FTPTime Fall Top Point Time FLPLevel Fall Low Point Level FMPLevel Fall Mid Point Level FHPLevel Fall High Point Level FTPLevel Fall Top Point Level
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.PulseEmodelItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:EMODel:X {param}')
