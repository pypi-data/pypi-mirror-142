from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DETect:LIMit \n
		Snippet: driver.applications.k6Pulse.sense.detect.limit.set(state = False) \n
		If enabled, the number of pulses to be detected is restricted. When the maximum number is exceeded, measurement is
		stopped for the current capture buffer. This limitation can be used to speed up the measurement if only a small number of
		pulses is of interest. The maximum number of pulses to be detected is defined using the [SENSe:]DETect:LIMit:COUNt
		command. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DETect:LIMit {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DETect:LIMit \n
		Snippet: value: bool = driver.applications.k6Pulse.sense.detect.limit.get() \n
		If enabled, the number of pulses to be detected is restricted. When the maximum number is exceeded, measurement is
		stopped for the current capture buffer. This limitation can be used to speed up the measurement if only a small number of
		pulses is of interest. The maximum number of pulses to be detected is defined using the [SENSe:]DETect:LIMit:COUNt
		command. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DETect:LIMit?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
