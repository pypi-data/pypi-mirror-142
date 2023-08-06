from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, modulation: enums.FrameModulation) -> None:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:PREVious:MODulation \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.previous.modulation.set(modulation = enums.FrameModulation.AUTO) \n
		Determines which modulation type is used to demodulate the frame previous to the first configured subframe. This command
		is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:param modulation: AUTO | DATA | PATTern Data The modulation type defined for data symbols is used (see [SENSe:]DDEMod:MAPPing[:VALue]) Pattern The modulation type defined for pattern symbols is used (see [SENSe:]DDEMod:PATTern:MAPPing[:VALue]) . Auto The previous frame uses the same modulation as the last subframe of the frame configuration.
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.FrameModulation)
		self._core.io.write(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:PREVious:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrameModulation:
		"""SCPI: [SENSe]:DDEMod:PATTern:FRAMe:EDIT:PREVious:MODulation \n
		Snippet: value: enums.FrameModulation = driver.applications.k70Vsa.sense.ddemod.pattern.frame.edit.previous.modulation.get() \n
		Determines which modulation type is used to demodulate the frame previous to the first configured subframe. This command
		is only available if the additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: modulation: AUTO | DATA | PATTern Data The modulation type defined for data symbols is used (see [SENSe:]DDEMod:MAPPing[:VALue]) Pattern The modulation type defined for pattern symbols is used (see [SENSe:]DDEMod:PATTern:MAPPing[:VALue]) . Auto The previous frame uses the same modulation as the last subframe of the frame configuration."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:FRAMe:EDIT:PREVious:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.FrameModulation)
