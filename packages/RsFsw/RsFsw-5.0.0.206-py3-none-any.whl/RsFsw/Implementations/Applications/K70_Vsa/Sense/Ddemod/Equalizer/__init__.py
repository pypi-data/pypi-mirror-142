from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Equalizer:
	"""Equalizer commands group definition. 7 total commands, 6 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("equalizer", core, parent)

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def load(self):
		"""load commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_load'):
			from .Load import Load
			self._load = Load(self._core, self._cmd_group)
		return self._load

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def save(self):
		"""save commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_save'):
			from .Save import Save
			self._save = Save(self._core, self._cmd_group)
		return self._save

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def reset(self) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:RESet \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.reset() \n
		This command deletes the data of the currently selected equalizer. After deletion, training can start again using the
		command DDEM:EQU:MODE TRA (see [SENSe:]DDEMod:EQUalizer:MODE) . \n
		"""
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:RESet \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.reset_with_opc() \n
		This command deletes the data of the currently selected equalizer. After deletion, training can start again using the
		command DDEM:EQU:MODE TRA (see [SENSe:]DDEMod:EQUalizer:MODE) . \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:DDEMod:EQUalizer:RESet', opc_timeout_ms)

	def clone(self) -> 'Equalizer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Equalizer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
