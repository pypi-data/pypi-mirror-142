from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Syntax:
	"""Syntax commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syntax", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def get(self, command: str) -> bytes:
		"""SCPI: SYSTem:HELP:SYNTax \n
		Snippet: value: bytes = driver.system.help.syntax.get(command = '1') \n
		No command help available \n
			:param command: No help available
			:return: syntax: No help available"""
		param = Conversions.value_to_quoted_str(command)
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:HELP:SYNTax? {param}')
		return response

	def clone(self) -> 'Syntax':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Syntax(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
