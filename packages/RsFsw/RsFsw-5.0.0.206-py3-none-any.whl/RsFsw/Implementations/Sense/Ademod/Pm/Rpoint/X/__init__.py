from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:ADEMod:PM:RPOint[:X] \n
		Snippet: driver.sense.ademod.pm.rpoint.x.set(time = 1.0) \n
		This command determines the position where the phase of the PM-demodulated signal is set to 0 rad. The maximum possible
		value depends on the measurement time selected in the instrument; this value is output in response to the query
		ADEM:PM:RPO:X? MAX. \n
			:param time: 0 s to measurement time Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:ADEMod:PM:RPOint:X {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:PM:RPOint[:X] \n
		Snippet: value: float = driver.sense.ademod.pm.rpoint.x.get() \n
		This command determines the position where the phase of the PM-demodulated signal is set to 0 rad. The maximum possible
		value depends on the measurement time selected in the instrument; this value is output in response to the query
		ADEM:PM:RPO:X? MAX. \n
			:return: time: 0 s to measurement time Unit: S"""
		response = self._core.io.query_str(f'SENSe:ADEMod:PM:RPOint:X?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'X':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = X(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
