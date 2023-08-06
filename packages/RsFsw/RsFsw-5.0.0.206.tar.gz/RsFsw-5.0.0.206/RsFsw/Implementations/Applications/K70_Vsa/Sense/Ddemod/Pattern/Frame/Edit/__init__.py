from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edit:
	"""Edit commands group definition. 8 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edit", core, parent)

	@property
	def next(self):
		"""next commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_next'):
			from .Next import Next
			self._next = Next(self._core, self._cmd_group)
		return self._next

	@property
	def previous(self):
		"""previous commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_previous'):
			from .Previous import Previous
			self._previous = Previous(self._core, self._cmd_group)
		return self._previous

	@property
	def structure(self):
		"""structure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_structure'):
			from .Structure import Structure
			self._structure = Structure(self._core, self._cmd_group)
		return self._structure

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Text import Text
			self._text = Text(self._core, self._cmd_group)
		return self._text

	def set(self, filename: str) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.set(filename = '1') \n
		Specifies an xml file for a user-defined frame structure configuration. The default storage location for such files is
		C:/R_S/INSTR/USER/vsa/FrameRangeStructure. This command is only available if the additional Multi-Modulation Analysis
		option (R&S FSW-K70M) is installed. If the specified file already exists, it is loaded for subsequent editing. Note that
		this command is a prerequisite to editing the frame structure of an existing file (using
		[SENSe:]DDEMod:PATTern:FRAMe:EDIT:STRucture or any other command starting with [SENS:]DDEM:PATT:FRAM:EDIT) . It does not
		load the file for use in the current measurement (see [SENSe:]DDEMod:PATTern:FRAMe:LOAD) . Therefore, you can edit a
		frame structure while simultaneously performing a measurement with another frame structure configuration. If the file
		does not yet exist, a new frame structure is created and will be stored to the specified file when the
		[SENSe:]DDEMod:PATTern:FRAMe:EDIT:SAVE command is executed. \n
			:param filename: string Path and file name of the xml file containing the frame structure configuration.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.get() \n
		Specifies an xml file for a user-defined frame structure configuration. The default storage location for such files is
		C:/R_S/INSTR/USER/vsa/FrameRangeStructure. This command is only available if the additional Multi-Modulation Analysis
		option (R&S FSW-K70M) is installed. If the specified file already exists, it is loaded for subsequent editing. Note that
		this command is a prerequisite to editing the frame structure of an existing file (using
		[SENSe:]DDEMod:PATTern:FRAMe:EDIT:STRucture or any other command starting with [SENS:]DDEM:PATT:FRAM:EDIT) . It does not
		load the file for use in the current measurement (see [SENSe:]DDEMod:PATTern:FRAMe:LOAD) . Therefore, you can edit a
		frame structure while simultaneously performing a measurement with another frame structure configuration. If the file
		does not yet exist, a new frame structure is created and will be stored to the specified file when the
		[SENSe:]DDEMod:PATTern:FRAMe:EDIT:SAVE command is executed. \n
			:return: filename: string Path and file name of the xml file containing the frame structure configuration."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:EDIT?')
		return trim_str_response(response)

	def save(self, filename: str = None) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:SAVE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.save(filename = '1') \n
		Stores the current frame structure configuration to the specified file. If no path is provided it is saved to the file
		selected previously by [SENSe:]DDEMod:PATTern:FRAMe:EDIT. This command is only available if the additional
		Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param filename: string Optional parameter: Path and file name of the xml file.
		"""
		param = ''
		if filename:
			param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:SAVE {param}'.strip())

	def clone(self) -> 'Edit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
