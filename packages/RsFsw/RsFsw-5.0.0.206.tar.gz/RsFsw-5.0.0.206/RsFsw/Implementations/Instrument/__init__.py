from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Instrument:
	"""Instrument commands group definition. 32 total commands, 8 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("instrument", core, parent)

	@property
	def create(self):
		"""create commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def selectName(self):
		"""selectName commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selectName'):
			from .SelectName import SelectName
			self._selectName = SelectName(self._core, self._cmd_group)
		return self._selectName

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def nselect(self):
		"""nselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nselect'):
			from .Nselect import Nselect
			self._nselect = Nselect(self._core, self._cmd_group)
		return self._nselect

	@property
	def rename(self):
		"""rename commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rename'):
			from .Rename import Rename
			self._rename = Rename(self._core, self._cmd_group)
		return self._rename

	@property
	def couple(self):
		"""couple commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_couple'):
			from .Couple import Couple
			self._couple = Couple(self._core, self._cmd_group)
		return self._couple

	def abort(self) -> None:
		"""SCPI: INSTrument:ABORt \n
		Snippet: driver.instrument.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'INSTrument:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INSTrument:ABORt \n
		Snippet: driver.instrument.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INSTrument:ABORt', opc_timeout_ms)

	def delete(self, channel_name: str) -> None:
		"""SCPI: INSTrument:DELete \n
		Snippet: driver.instrument.delete(channel_name = r1) \n
		This command deletes a channel. If you delete the last channel, the default 'Spectrum' channel is activated. \n
			:param channel_name: String containing the name of the channel you want to delete. A channel must exist in order to be able delete it.
		"""
		param = Conversions.value_to_str(channel_name)
		self._core.io.write_with_opc(f'INSTrument:DELete {param}')

	def clone(self) -> 'Instrument':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Instrument(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
