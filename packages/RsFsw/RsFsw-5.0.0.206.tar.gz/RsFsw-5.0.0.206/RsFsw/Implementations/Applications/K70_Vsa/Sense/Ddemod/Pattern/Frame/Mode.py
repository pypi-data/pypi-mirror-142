from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, frame_mode: enums.ConfigMode) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:MODE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.mode.set(frame_mode = enums.ConfigMode.DEFault) \n
		Determines whether the frame structure of the signal is configured in reference to the result range or user-defined. This
		command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param frame_mode: DEFault | USER Default A single frame is assumed to correspond to the result range defined by [SENSe:]DDEMod:TIME. User-Defined A frame is defined manually as a succession of subframes with specified characteristics. In this case, the result range is assumed to be a single frame as specified by [SENSe:]DDEMod:PATTern:FRAMe:EDIT:STRucture. If no structure is configured or loaded yet, the result range definition is used (as for 'Default') .
		"""
		param = Conversions.enum_scalar_to_str(frame_mode, enums.ConfigMode)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ConfigMode:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:MODE \n
		Snippet: value: enums.ConfigMode = driver.applications.k70Vsa.sense.ddemod.pattern.frame.mode.get() \n
		Determines whether the frame structure of the signal is configured in reference to the result range or user-defined. This
		command is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: frame_mode: DEFault | USER Default A single frame is assumed to correspond to the result range defined by [SENSe:]DDEMod:TIME. User-Defined A frame is defined manually as a succession of subframes with specified characteristics. In this case, the result range is assumed to be a single frame as specified by [SENSe:]DDEMod:PATTern:FRAMe:EDIT:STRucture. If no structure is configured or loaded yet, the result range definition is used (as for 'Default') ."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ConfigMode)
