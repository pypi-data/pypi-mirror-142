from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtime:
	"""Mtime commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtime", core, parent)

	@property
	def average(self):
		"""average commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	def set(self, duration: enums.Duration) -> None:
		"""SCPI: [SENSe]:PMETer:MTIMe \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.mtime.set(duration = enums.Duration.LONG) \n
		This command selects the duration of power sensor measurements. \n
			:param duration: SHORt | NORMal | LONG
		"""
		param = Conversions.enum_scalar_to_str(duration, enums.Duration)
		self._core.io.write(f'SENSe:PMETer:MTIMe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Duration:
		"""SCPI: [SENSe]:PMETer:MTIMe \n
		Snippet: value: enums.Duration = driver.applications.k18AmplifierEt.sense.pmeter.mtime.get() \n
		This command selects the duration of power sensor measurements. \n
			:return: duration: SHORt | NORMal | LONG"""
		response = self._core.io.query_str(f'SENSe:PMETer:MTIMe?')
		return Conversions.str_to_scalar_enum(response, enums.Duration)

	def clone(self) -> 'Mtime':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mtime(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
