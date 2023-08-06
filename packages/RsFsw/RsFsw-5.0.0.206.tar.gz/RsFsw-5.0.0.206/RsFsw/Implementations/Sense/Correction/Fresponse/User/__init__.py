from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 40 total commands, 12 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def spectrum(self):
		"""spectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def fstate(self):
		"""fstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fstate'):
			from .Fstate import Fstate
			self._fstate = Fstate(self._core, self._cmd_group)
		return self._fstate

	@property
	def scope(self):
		"""scope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scope'):
			from .Scope import Scope
			self._scope = Scope(self._core, self._cmd_group)
		return self._scope

	@property
	def valid(self):
		"""valid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_valid'):
			from .Valid import Valid
			self._valid = Valid(self._core, self._cmd_group)
		return self._valid

	@property
	def scovered(self):
		"""scovered commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scovered'):
			from .Scovered import Scovered
			self._scovered = Scovered(self._core, self._cmd_group)
		return self._scovered

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	@property
	def flist(self):
		"""flist commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_flist'):
			from .Flist import Flist
			self._flist = Flist(self._core, self._cmd_group)
		return self._flist

	@property
	def slist(self):
		"""slist commands group. 8 Sub-classes, 2 commands."""
		if not hasattr(self, '_slist'):
			from .Slist import Slist
			self._slist = Slist(self._core, self._cmd_group)
		return self._slist

	@property
	def pstate(self):
		"""pstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pstate'):
			from .Pstate import Pstate
			self._pstate = Pstate(self._core, self._cmd_group)
		return self._pstate

	def preset(self) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:PRESet \n
		Snippet: driver.sense.correction.fresponse.user.preset() \n
		Restores the default frequency response correction settings (containing only files specific to the R&S FSW itself) .
		Frequency response correction using .fres files is deactivated. \n
		"""
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:PRESet \n
		Snippet: driver.sense.correction.fresponse.user.preset_with_opc() \n
		Restores the default frequency response correction settings (containing only files specific to the R&S FSW itself) .
		Frequency response correction using .fres files is deactivated. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:USER:PRESet', opc_timeout_ms)

	def load(self, file_path: str) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:LOAD \n
		Snippet: driver.sense.correction.fresponse.user.load(file_path = '1') \n
		Loads a stored user-defined frequency response correction scenario. \n
			:param file_path: string
		"""
		param = Conversions.value_to_quoted_str(file_path)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:LOAD {param}')

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
