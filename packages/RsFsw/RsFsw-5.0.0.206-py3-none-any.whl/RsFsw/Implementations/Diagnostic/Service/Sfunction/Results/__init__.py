from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Results:
	"""Results commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("results", core, parent)

	@property
	def save(self):
		"""save commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_save'):
			from .Save import Save
			self._save = Save(self._core, self._cmd_group)
		return self._save

	def delete(self) -> None:
		"""SCPI: DIAGnostic:SERVice:SFUNction:RESults:DELete \n
		Snippet: driver.diagnostic.service.sfunction.results.delete() \n
		This command deletes the results of the most recent service function you have used. \n
		"""
		self._core.io.write(f'DIAGnostic:SERVice:SFUNction:RESults:DELete')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:SERVice:SFUNction:RESults:DELete \n
		Snippet: driver.diagnostic.service.sfunction.results.delete_with_opc() \n
		This command deletes the results of the most recent service function you have used. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:SERVice:SFUNction:RESults:DELete', opc_timeout_ms)

	def clone(self) -> 'Results':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Results(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
