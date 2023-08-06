from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequencer:
	"""Sequencer commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def refresh(self):
		"""refresh commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_refresh'):
			from .Refresh import Refresh
			self._refresh = Refresh(self._core, self._cmd_group)
		return self._refresh

	def abort(self) -> None:
		"""SCPI: INITiate:SEQuencer:ABORt \n
		Snippet: driver.initiate.sequencer.abort() \n
		This command stops the currently active sequence of measurements. You can start a new sequence any time using method
		RsFsw.Initiate.Sequencer.Immediate.set. \n
		"""
		self._core.io.write(f'INITiate:SEQuencer:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:SEQuencer:ABORt \n
		Snippet: driver.initiate.sequencer.abort_with_opc() \n
		This command stops the currently active sequence of measurements. You can start a new sequence any time using method
		RsFsw.Initiate.Sequencer.Immediate.set. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:SEQuencer:ABORt', opc_timeout_ms)

	def clone(self) -> 'Sequencer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequencer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
