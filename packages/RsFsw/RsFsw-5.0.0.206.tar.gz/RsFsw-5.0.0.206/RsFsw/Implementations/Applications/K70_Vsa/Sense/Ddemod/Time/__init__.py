from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, result_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:TIME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.time.set(result_length = 1.0) \n
		The command determines the number of displayed symbols (result length) . \n
			:param result_length: numeric value Range: 10 to 64000, Unit: Sym
		"""
		param = Conversions.decimal_value_to_str(result_length)
		self._core.io.write(f'SENSe:DDEMod:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:TIME \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.time.get() \n
		The command determines the number of displayed symbols (result length) . \n
			:return: result_length: numeric value Range: 10 to 64000, Unit: Sym"""
		response = self._core.io.query_str(f'SENSe:DDEMod:TIME?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Time':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Time(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
