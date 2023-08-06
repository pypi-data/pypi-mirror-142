from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	def set(self, yaxis: enums.AxisPower, xaxis: enums.HopXaxisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:POWer \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.power.set(yaxis = enums.AxisPower.AVGPower, xaxis = enums.HopXaxisItems.AVGFm, window = repcap.Window.Default) \n
		Configures the x-axis and y-axis of the Parameter Trend result display for hop trends over time. \n
			:param yaxis: AVGPower | MAXPower | MINPower | PWRRipple MINPower Minimum power MAXPower Maximum power AVGPower Average power PWRRipple Power ripple
			:param xaxis: AVGFm | FMERror | FREQuency | MAXFm | RELFrequency | RMSFm | FMSLength | FMSPoint | FMSTime | AVPHm | MXPHm | RMSPm | PMSLength | PMSPoint | PMSTime | AVGPower | MAXPower | MINPower | PWRRipple | INDex | STAFrequency | BEGin | DWELl | SWITching FREQuency Average frequency RELFrequency Relative frequency (hop-to-hop) FMERror Hop state deviation MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length AVPHm Average phase deviation MXPHm Maximum phase deviation RMSPm RMS phase deviation PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length MINPower Minimum power MAXPower Maximum power AVGPower Average power PWRRipple Power ripple INDex Hop index STAFrequency State frequency (nominal) BEGin Hop Begin DWELl Hop dwell time SWITching Switching time
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('yaxis', yaxis, DataType.Enum, enums.AxisPower), ArgSingle('xaxis', xaxis, DataType.Enum, enums.HopXaxisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:POWer {param}'.rstrip())

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
