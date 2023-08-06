from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tags:
	"""Tags commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tags", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	def delete(self, delete_tag: str) -> None:
		"""SCPI: DIAGnostic:HUMS:TAGS:DELete \n
		Snippet: driver.diagnostic.hums.tags.delete(delete_tag = '1') \n
		This command deletes a certain tag you assigned to your instrument, including its key and value. \n
			:param delete_tag: ID number of the tag you want to delete. To identify the ID number, query all device tags from the system first. For more information, see method RsFsw.Diagnostic.Hums.Tags.All.get_.
		"""
		param = Conversions.value_to_quoted_str(delete_tag)
		self._core.io.write(f'DIAGnostic:HUMS:TAGS:DELete {param}')

	def delete_all(self) -> None:
		"""SCPI: DIAGnostic:HUMS:TAGS:DELete:ALL \n
		Snippet: driver.diagnostic.hums.tags.delete_all() \n
		This command deletes all key-value tags you have assigned to the instrument. \n
		"""
		self._core.io.write(f'DIAGnostic:HUMS:TAGS:DELete:ALL')

	def delete_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:HUMS:TAGS:DELete:ALL \n
		Snippet: driver.diagnostic.hums.tags.delete_all_with_opc() \n
		This command deletes all key-value tags you have assigned to the instrument. \n
		Same as delete_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:HUMS:TAGS:DELete:ALL', opc_timeout_ms)

	def clone(self) -> 'Tags':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tags(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
