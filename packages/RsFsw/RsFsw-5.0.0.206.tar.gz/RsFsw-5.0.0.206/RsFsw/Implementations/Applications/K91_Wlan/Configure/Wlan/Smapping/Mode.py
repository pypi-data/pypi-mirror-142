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

	def set(self, mode: enums.SpecialMappingMode) -> None:
		"""SCPI: CONFigure:WLAN:SMAPping:MODE \n
		Snippet: driver.applications.k91Wlan.configure.wlan.smapping.mode.set(mode = enums.SpecialMappingMode.DIRect) \n
		This remote control command specifies the special mapping mode. \n
			:param mode: DIRect | SEXPansion | USER DIRect direct SEXPansion expansion USER user defined
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SpecialMappingMode)
		self._core.io.write(f'CONFigure:WLAN:SMAPping:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SpecialMappingMode:
		"""SCPI: CONFigure:WLAN:SMAPping:MODE \n
		Snippet: value: enums.SpecialMappingMode = driver.applications.k91Wlan.configure.wlan.smapping.mode.get() \n
		This remote control command specifies the special mapping mode. \n
			:return: mode: DIRect | SEXPansion | USER DIRect direct SEXPansion expansion USER user defined"""
		response = self._core.io.query_str(f'CONFigure:WLAN:SMAPping:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SpecialMappingMode)
