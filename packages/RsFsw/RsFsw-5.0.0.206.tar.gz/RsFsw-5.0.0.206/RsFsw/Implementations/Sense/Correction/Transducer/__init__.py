from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transducer:
	"""Transducer commands group definition. 13 total commands, 11 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transducer", core, parent)

	@property
	def generate(self):
		"""generate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_generate'):
			from .Generate import Generate
			self._generate = Generate(self._core, self._cmd_group)
		return self._generate

	@property
	def active(self):
		"""active commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_active'):
			from .Active import Active
			self._active = Active(self._core, self._cmd_group)
		return self._active

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def scaling(self):
		"""scaling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scaling'):
			from .Scaling import Scaling
			self._scaling = Scaling(self._core, self._cmd_group)
		return self._scaling

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
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	def delete(self) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:DELete \n
		Snippet: driver.sense.correction.transducer.delete() \n
		This command deletes the currently selected transducer factor. Before you can use the command, you have to select a
		transducer. \n
		"""
		self._core.io.write(f'SENSe:CORRection:TRANsducer:DELete')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:DELete \n
		Snippet: driver.sense.correction.transducer.delete_with_opc() \n
		This command deletes the currently selected transducer factor. Before you can use the command, you have to select a
		transducer. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:TRANsducer:DELete', opc_timeout_ms)

	def clone(self) -> 'Transducer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Transducer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
