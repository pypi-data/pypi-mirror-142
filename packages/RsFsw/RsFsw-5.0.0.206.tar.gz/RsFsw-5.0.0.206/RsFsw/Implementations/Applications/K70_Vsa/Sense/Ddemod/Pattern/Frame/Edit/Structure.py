from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Structure:
	"""Structure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("structure", core, parent)

	# noinspection PyTypeChecker
	class StructureStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Name: List[str]: string Name of the subframe. Duplicate names are allowed.
			- Nof_Symbols: List[float]: integer The number of symbols the subframe consists of. For pattern subframes, the number of symbols must correspond to the number of symbols defined using[SENSe:]DDEMod:SEARch:SYNC:DATA.
			- Modulation: List[enums.FrameModulationB]: DATA | PATTern Determines which modulation type is used to demodulate the subframe. The modulation for the 'previous frame' and 'next frame' are defined by separate commands (see [SENSe:]DDEMod:PATTern:FRAMe:EDIT:PREVious:MODulation and [SENSe:]DDEMod:PATTern:FRAMe:EDIT:NEXT:MODulation) . DATA The modulation type defined for data symbols is used (see [SENSe:]DDEMod:MAPPing[:VALue]) . PATTern The modulation type defined for patterns is used (see [SENSe:]DDEMod:PATTern:MAPPing[:VALue]) .
			- Type_Py: List[enums.FrameModulationB]: DATA | PATTern Determines whether the demodulated data in the subframe is known or unknown by the R&S FSW VSA application. PATTern The data is assumed to correspond with the pattern definition (see [SENSe:]DDEMod:SEARch:SYNC:DATA) . Not available for modulation type: 'DATA'. Only one subframe is allowed to be of type 'PATTern'. DATA The data is unknown. Used for data symbols or header information.
			- Boosting: List[float]: numeric value For subframes with gain values different to the data symbols, define a different boosting factor to be applied to the reference power. Range: 0.1 to 60
			- Description: List[str]: string Description for an individual subframe. Use an empty string ('') to leave out the description."""
		__meta_args_list = [
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Nof_Symbols', DataType.FloatList, None, False, True, 1),
			ArgStruct('Modulation', DataType.EnumList, enums.FrameModulationB, False, True, 1),
			ArgStruct('Type_Py', DataType.EnumList, enums.FrameModulationB, False, True, 1),
			ArgStruct('Boosting', DataType.FloatList, None, False, True, 1),
			ArgStruct('Description', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name: List[str] = None
			self.Nof_Symbols: List[float] = None
			self.Modulation: List[enums.FrameModulationB] = None
			self.Type_Py: List[enums.FrameModulationB] = None
			self.Boosting: List[float] = None
			self.Description: List[str] = None

	def set(self, structure: StructureStruct) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:STRucture \n
		Snippet with structure: \n
		structure = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.structure.StructureStruct() \n
		structure.Name: List[str] = ['1', '2', '3'] \n
		structure.Nof_Symbols: List[float] = [1.1, 2.2, 3.3] \n
		structure.Modulation: List[enums.FrameModulationB] = [FrameModulationB.DATA, FrameModulationB.PATTern] \n
		structure.Type_Py: List[enums.FrameModulationB] = [FrameModulationB.DATA, FrameModulationB.PATTern] \n
		structure.Boosting: List[float] = [1.1, 2.2, 3.3] \n
		structure.Description: List[str] = ['1', '2', '3'] \n
		driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.structure.set(structure) \n
		Defines the frame structure for a previously loaded file. For each subframe, all parameters must be defined. This command
		is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. Note that the file must
		be loaded for editing before the structure can be defined using this command (see [SENSe:]DDEMod:PATTern:FRAMe:EDIT) .
		Loading the file for use in the current measurement is not sufficient (see [SENSe:]DDEMod:PATTern:FRAMe:LOAD) . Therefore,
		you can edit a frame structure while simultaneously performing a measurement with another frame structure configuration.
		The configuration is only stored by a subsequent [SENSe:]DDEMod:PATTern:FRAMe:EDIT:SAVE command. The modulation for the
		'previous frame' and 'next frame' are defined by separate commands (see [SENS:]DDEM:PATT:FRAM:PREV:...
		and [SENS:]DDEM:PATT:FRAM:NEXT:...) . \n
			:param structure: for set value, see the help for StructureStruct structure arguments.
		"""
		self._core.io.write_struct(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:STRucture', structure)

	def get(self) -> StructureStruct:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:STRucture \n
		Snippet: value: StructureStruct = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.structure.get() \n
		Defines the frame structure for a previously loaded file. For each subframe, all parameters must be defined. This command
		is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. Note that the file must
		be loaded for editing before the structure can be defined using this command (see [SENSe:]DDEMod:PATTern:FRAMe:EDIT) .
		Loading the file for use in the current measurement is not sufficient (see [SENSe:]DDEMod:PATTern:FRAMe:LOAD) . Therefore,
		you can edit a frame structure while simultaneously performing a measurement with another frame structure configuration.
		The configuration is only stored by a subsequent [SENSe:]DDEMod:PATTern:FRAMe:EDIT:SAVE command. The modulation for the
		'previous frame' and 'next frame' are defined by separate commands (see [SENS:]DDEM:PATT:FRAM:PREV:...
		and [SENS:]DDEM:PATT:FRAM:NEXT:...) . \n
			:return: structure: for return value, see the help for StructureStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:STRucture?', self.__class__.StructureStruct())
