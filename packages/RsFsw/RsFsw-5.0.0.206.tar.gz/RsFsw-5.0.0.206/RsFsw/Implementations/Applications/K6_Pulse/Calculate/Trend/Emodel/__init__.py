from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emodel:
	"""Emodel commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emodel", core, parent)

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	def set(self, yaxis: enums.PulseEmodelItems, xaxis: enums.PulseAxisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:EMODel \n
		Snippet: driver.applications.k6Pulse.calculate.trend.emodel.set(yaxis = enums.PulseEmodelItems.FBPTime, xaxis = enums.PulseAxisItems.DCYCle, window = repcap.Window.Default) \n
		Configures the Parameter Trend result display for envelope model trends. This command defines both x-axis and y-axis
		parameters in one step. It is equivalent to the two subsequent commands: CALCulate<n>:TRENd:EMODel:X TSTamp | PNUMber
		(see method RsFsw.Applications.K6_Pulse.Calculate.Trend.Emodel.X.set) CALCulate<n>:TRENd:EMODel:Y <YAxis> (see method
		RsFsw.Applications.K6_Pulse.Calculate.Trend.Emodel.Y.set) \n
			:param yaxis: RBPTime | RLPTime | RMPTime | RHPTime | RTPTime | RLPLevel | RMPLevel | RHPLevel | RTPLevel | FBPTime | FLPTime | FMPTime | FHPTime | FTPTime | FLPLevel | FMPLevel | FHPLevel | FTPLevel RBPTime Rise Base Point Time RLPTime Rise Low Point Time RMPTime Rise Mid Point Time RHPTime Rise High Point Time RTPTime Rise Top Point Time RLPLevel Rise Low Point Level RMPLevel Rise Mid Point Level RHPLevel Rise High Point Level RTPLevel Rise Top Point Level FBPTime Fall Base Point Time FLPTime Fall Low Point Time FMPTime Fall Mid Point Time FHPTime Fall High Point Time FTPTime Fall Top Point Time FLPLevel Fall Low Point Level FMPLevel Fall Mid Point Level FHPLevel Fall High Point Level FTPLevel Fall Top Point Level
			:param xaxis: PNUMber | TSTamp | SETTling | RISE | FALL | PWIDth | OFF | DRATio | DCYCle | PRI | PRF Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Timing parameters'. TSTamp Timestamp PNUMber The pulse numbers are represented on the x-axis (available numbers can be queried using [SENSe:]PULSe:NUMBer?) . Intervals without pulses are not displayed. SETTling Settling Time RISE Rise Time FALL Fall Time PWIDth Pulse Width (ON Time) OFF Off Time DRATio Duty Ratio DCYCle Duty Cycle (%) PRI Pulse Repetition Interval PRF Pulse Repetition Frequency (Hz)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('yaxis', yaxis, DataType.Enum, enums.PulseEmodelItems), ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulseAxisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:EMODel {param}'.rstrip())

	def clone(self) -> 'Emodel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emodel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
