from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:WLAN:GTIMe:AUTO \n
		Snippet: driver.applications.k91Wlan.configure.wlan.gtime.auto.set(state = False) \n
		This remote control command specifies whether the guard time of the input signal is automatically detected or specified
		manually (IEEE 802.11n or ac only) . \n
			:param state: ON | 1 The guard time is detected automatically according to method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Auto.TypePy.set. OFF | 0 The guard time is defined by the method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Select.set command.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:WLAN:GTIMe:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:WLAN:GTIMe:AUTO \n
		Snippet: value: bool = driver.applications.k91Wlan.configure.wlan.gtime.auto.get() \n
		This remote control command specifies whether the guard time of the input signal is automatically detected or specified
		manually (IEEE 802.11n or ac only) . \n
			:return: state: ON | 1 The guard time is detected automatically according to method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Auto.TypePy.set. OFF | 0 The guard time is defined by the method RsFsw.Applications.K91_Wlan.Configure.Wlan.Gtime.Select.set command."""
		response = self._core.io.query_str(f'CONFigure:WLAN:GTIMe:AUTO?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Auto':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Auto(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
