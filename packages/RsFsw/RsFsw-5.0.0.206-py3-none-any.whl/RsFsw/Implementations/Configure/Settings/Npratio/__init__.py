from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npratio:
	"""Npratio commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npratio", core, parent)

	@property
	def notch(self):
		"""notch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import Notch
			self._notch = Notch(self._core, self._cmd_group)
		return self._notch

	def set(self) -> None:
		"""SCPI: CONFigure:SETTings:NPRatio \n
		Snippet: driver.configure.settings.npratio.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:SETTings:NPRatio')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:SETTings:NPRatio \n
		Snippet: driver.configure.settings.npratio.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:SETTings:NPRatio', opc_timeout_ms)

	def clone(self) -> 'Npratio':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Npratio(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
