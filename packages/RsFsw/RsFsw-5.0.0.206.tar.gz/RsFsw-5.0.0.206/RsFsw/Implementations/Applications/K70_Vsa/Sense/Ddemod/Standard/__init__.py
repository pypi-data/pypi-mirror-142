from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 6 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import Comment
			self._comment = Comment(self._core, self._cmd_group)
		return self._comment

	@property
	def preset(self):
		"""preset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def save(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:SAVE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.save(filename = '1') \n
		This command stores the current settings of the vector signal analysis as a new user-defined digital standard.
		If the name of the digital standard is already in use, an error message is output and a new name has to be selected.
		It is recommended that you define a comment before storing the standard. \n
			:param filename: The path and file name to which the settings are stored.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:STANdard:SAVE {param}')

	def delete(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:DELete \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.delete(filename = '1') \n
		This command deletes a specified digital standard file in the vector signal analysis. \n
			:param filename: File name including the path for the digital standard file
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:STANdard:DELete {param}')

	def clone(self) -> 'Standard':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Standard(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
