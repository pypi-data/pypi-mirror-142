from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import Remove
			self._remove = Remove(self._core, self._cmd_group)
		return self._remove

	def set(self, arg_0: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:PATTern \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.pattern.set(arg_0 = '1') \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:PATTern {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:PATTern \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.pattern.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:PATTern?')
		return trim_str_response(response)

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
