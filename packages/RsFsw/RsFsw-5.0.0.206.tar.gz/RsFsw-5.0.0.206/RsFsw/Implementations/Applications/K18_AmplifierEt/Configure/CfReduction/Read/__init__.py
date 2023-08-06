from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self) -> None:
		"""SCPI: CONFigure:CFReduction:READ \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.read.set() \n
		Applies crest factor reduction on the connected signal generator. \n
		"""
		self._core.io.write(f'CONFigure:CFReduction:READ')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:CFReduction:READ \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.read.set_with_opc() \n
		Applies crest factor reduction on the connected signal generator. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:CFReduction:READ', opc_timeout_ms)

	def clone(self) -> 'Read':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Read(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
