from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 18 total commands, 14 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def nstate(self):
		"""nstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nstate'):
			from .Nstate import Nstate
			self._nstate = Nstate(self._core, self._cmd_group)
		return self._nstate

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Text import Text
			self._text = Text(self._core, self._cmd_group)
		return self._text

	@property
	def found(self):
		"""found commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_found'):
			from .Found import Found
			self._found = Found(self._core, self._cmd_group)
		return self._found

	@property
	def iqcThreshold(self):
		"""iqcThreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqcThreshold'):
			from .IqcThreshold import IqcThreshold
			self._iqcThreshold = IqcThreshold(self._core, self._cmd_group)
		return self._iqcThreshold

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def pattern(self):
		"""pattern commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def copy(self, pattern: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:COPY \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.copy(pattern = '1') \n
		This command copies a pattern file. The pattern to be copied must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. Tip: In manual operation, a pattern can be copied in the editor by storing it under a
		new name. \n
			:param pattern: No help available
		"""
		param = Conversions.value_to_quoted_str(pattern)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:COPY {param}')

	def delete(self) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:DELete \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.delete() \n
		This command deletes a sync sequence. The sync sequence to be deleted must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. \n
		"""
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:DELete')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:DELete \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.delete_with_opc() \n
		This command deletes a sync sequence. The sync sequence to be deleted must have been selected before using
		[SENSe:]DDEMod:SEARch:SYNC:NAME. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:DDEMod:SEARch:SYNC:DELete', opc_timeout_ms)

	def clone(self) -> 'Sync':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sync(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
