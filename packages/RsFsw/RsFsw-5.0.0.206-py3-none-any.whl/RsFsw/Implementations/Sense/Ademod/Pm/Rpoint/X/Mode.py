from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.PmRpointMode) -> None:
		"""SCPI: [SENSe]:ADEMod:PM:RPOint[:X]:MODE \n
		Snippet: driver.sense.ademod.pm.rpoint.x.mode.set(mode = enums.PmRpointMode.MANual) \n
		Defines how the reference position in time for 0 rad is determined. \n
			:param mode: MANual | RIGHt MANual The time is defined using [SENSe:]ADEMod:PM:RPOint[:X]. RIGHt The time of the last measured value is used as the reference position. The time of the last measured value corresponds to the acquisition time, with respect to the trigger event and trigger offset, if applicable. If the acquistion time or the trigger values are changed, the reference position is automatically adapted.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PmRpointMode)
		self._core.io.write(f'SENSe:ADEMod:PM:RPOint:X:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PmRpointMode:
		"""SCPI: [SENSe]:ADEMod:PM:RPOint[:X]:MODE \n
		Snippet: value: enums.PmRpointMode = driver.sense.ademod.pm.rpoint.x.mode.get() \n
		Defines how the reference position in time for 0 rad is determined. \n
			:return: mode: MANual | RIGHt MANual The time is defined using [SENSe:]ADEMod:PM:RPOint[:X]. RIGHt The time of the last measured value is used as the reference position. The time of the last measured value corresponds to the acquisition time, with respect to the trigger event and trigger offset, if applicable. If the acquistion time or the trigger values are changed, the reference position is automatically adapted."""
		response = self._core.io.query_str(f'SENSe:ADEMod:PM:RPOint:X:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PmRpointMode)
