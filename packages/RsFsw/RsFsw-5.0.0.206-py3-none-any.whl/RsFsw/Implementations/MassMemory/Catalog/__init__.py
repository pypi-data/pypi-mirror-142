from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	@property
	def long(self):
		"""long commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_long'):
			from .Long import Long
			self._long = Long(self._core, self._cmd_group)
		return self._long

	def get(self) -> str:
		"""SCPI: MMEMory:CATalog \n
		Snippet: value: str = driver.massMemory.catalog.get() \n
		This command returns the contents of a particular directory. \n
			:return: filename: String containing the path and directory If you leave out the path, the command returns the contents of the directory selected with method RsFsw.MassMemory.CurrentDirectory.set. The path may be relative or absolute. Using wildcards ('*') is possible to query a certain type of files only. If you use a specific file as a parameter, the command returns the name of the file if the file is found in the specified directory, or an error if the file is not found ('-256,'File name not found') ."""
		response = self._core.io.query_str(f'MMEMory:CATalog?')
		return trim_str_response(response)

	def clone(self) -> 'Catalog':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Catalog(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
