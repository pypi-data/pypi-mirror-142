from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	@property
	def calibration(self):
		"""calibration commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	def set(self, mode: bool) -> None:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: driver.applications.k91Wlan.configure.power.auto.set(mode = False) \n
		This command is used to switch on or off automatic power level detection. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]ADJust:LEVel for new remote control programs. \n
			:param mode: ON Automatic power level detection is performed at the start of each measurement sweep, and the reference level is adapted accordingly. OFF The reference level must be defined manually (see method RsFsw.Applications.K60_Transient.Display.Window.Trace.Y.Scale.RefLevel.set) ONCE Automatic power level detection is performed once at the start of the next measurement sweep, and the reference level is adapted accordingly.
		"""
		param = Conversions.bool_to_str(mode)
		self._core.io.write(f'CONFigure:POWer:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: value: bool = driver.applications.k91Wlan.configure.power.auto.get() \n
		This command is used to switch on or off automatic power level detection. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]ADJust:LEVel for new remote control programs. \n
			:return: mode: ON Automatic power level detection is performed at the start of each measurement sweep, and the reference level is adapted accordingly. OFF The reference level must be defined manually (see method RsFsw.Applications.K60_Transient.Display.Window.Trace.Y.Scale.RefLevel.set) ONCE Automatic power level detection is performed once at the start of the next measurement sweep, and the reference level is adapted accordingly."""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Auto':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Auto(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
