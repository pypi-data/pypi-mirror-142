from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.NpRatioMode) -> None:
		"""SCPI: [SENSe]:NPRatio:MODE \n
		Snippet: driver.sense.npratio.mode.set(mode = enums.NpRatioMode.DENSity) \n
		Determines whether the power measured in a channel or notch is indicated as a power or a density value. \n
			:param mode: POWer | DENSity DENSity Power measured in channel or notch divided by the 'Channel BW'/'Integration BW' in dBm/Hz POWer Absolute power measured in channel or notch in current amplitude unit
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NpRatioMode)
		self._core.io.write(f'SENSe:NPRatio:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.NpRatioMode:
		"""SCPI: [SENSe]:NPRatio:MODE \n
		Snippet: value: enums.NpRatioMode = driver.sense.npratio.mode.get() \n
		Determines whether the power measured in a channel or notch is indicated as a power or a density value. \n
			:return: mode: POWer | DENSity DENSity Power measured in channel or notch divided by the 'Channel BW'/'Integration BW' in dBm/Hz POWer Absolute power measured in channel or notch in current amplitude unit"""
		response = self._core.io.query_str(f'SENSe:NPRatio:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NpRatioMode)
