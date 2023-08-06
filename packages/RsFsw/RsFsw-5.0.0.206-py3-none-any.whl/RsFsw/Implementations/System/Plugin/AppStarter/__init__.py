from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AppStarter:
	"""AppStarter commands group definition. 8 total commands, 7 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("appStarter", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	@property
	def params(self):
		"""params commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_params'):
			from .Params import Params
			self._params = Params(self._core, self._cmd_group)
		return self._params

	@property
	def directory(self):
		"""directory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_directory'):
			from .Directory import Directory
			self._directory = Directory(self._core, self._cmd_group)
		return self._directory

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def icon(self):
		"""icon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icon'):
			from .Icon import Icon
			self._icon = Icon(self._core, self._cmd_group)
		return self._icon

	def delete(self, application_group: str, display_name: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:DELete \n
		Snippet: driver.system.plugin.appStarter.delete(application_group = '1', display_name = '1') \n
		Removes the specified application from the Application Starter dialog box. \n
			:param application_group: 'External' | 'User' The group (tab) of applications in the Application Starter that the application belongs to. 'External' External Applications 'User' User Applications
			:param display_name: Name of the application in the Application Starter
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('application_group', application_group, DataType.String), ArgSingle('display_name', display_name, DataType.String))
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:DELete {param}'.rstrip())

	def clone(self) -> 'AppStarter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AppStarter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
