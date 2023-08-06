from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MassMemory:
	"""MassMemory commands group definition. 75 total commands, 14 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("massMemory", core, parent)

	@property
	def clear(self):
		"""clear commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import Clear
			self._clear = Clear(self._core, self._cmd_group)
		return self._clear

	@property
	def load(self):
		"""load commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_load'):
			from .Load import Load
			self._load = Load(self._core, self._cmd_group)
		return self._load

	@property
	def store(self):
		"""store commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	@property
	def currentDirectory(self):
		"""currentDirectory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_currentDirectory'):
			from .CurrentDirectory import CurrentDirectory
			self._currentDirectory = CurrentDirectory(self._core, self._cmd_group)
		return self._currentDirectory

	@property
	def network(self):
		"""network commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_network'):
			from .Network import Network
			self._network = Network(self._core, self._cmd_group)
		return self._network

	@property
	def select(self):
		"""select commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def raw(self):
		"""raw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_raw'):
			from .Raw import Raw
			self._raw = Raw(self._core, self._cmd_group)
		return self._raw

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def delete(self):
		"""delete commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_delete'):
			from .Delete import Delete
			self._delete = Delete(self._core, self._cmd_group)
		return self._delete

	@property
	def makeDirectory(self):
		"""makeDirectory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_makeDirectory'):
			from .MakeDirectory import MakeDirectory
			self._makeDirectory = MakeDirectory(self._core, self._cmd_group)
		return self._makeDirectory

	@property
	def msis(self):
		"""msis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_msis'):
			from .Msis import Msis
			self._msis = Msis(self._core, self._cmd_group)
		return self._msis

	@property
	def deleteDirectory(self):
		"""deleteDirectory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deleteDirectory'):
			from .DeleteDirectory import DeleteDirectory
			self._deleteDirectory = DeleteDirectory(self._core, self._cmd_group)
		return self._deleteDirectory

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	def clear_all(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MMEMory:CLEar:ALL \n
		Snippet: driver.massMemory.clear_all() \n
		This command deletes all instrument configuration files in the current directory. You can select the directory with
		method RsFsw.MassMemory.CurrentDirectory.set. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MMEMory:CLEar:ALL', opc_timeout_ms)

	def copy(self, source_file: str, target_file: str) -> None:
		"""SCPI: MMEMory:COPY \n
		Snippet: driver.massMemory.copy(source_file = '1', target_file = '1') \n
		This command copies one or more files to another directory. \n
			:param source_file: No help available
			:param target_file: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_file', source_file, DataType.String), ArgSingle('target_file', target_file, DataType.String))
		self._core.io.write_with_opc(f'MMEMory:COPY {param}'.rstrip())

	def move(self, source_file: str, target_file: str) -> None:
		"""SCPI: MMEMory:MOVE \n
		Snippet: driver.massMemory.move(source_file = '1', target_file = '1') \n
		This command moves a file to another directory. The command also renames the file if you define a new name in the target
		directory. If you do not include a path for <NewFileName>, the command just renames the file. \n
			:param source_file: No help available
			:param target_file: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_file', source_file, DataType.String), ArgSingle('target_file', target_file, DataType.String))
		self._core.io.write_with_opc(f'MMEMory:MOVE {param}'.rstrip())

	def clone(self) -> 'MassMemory':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MassMemory(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
