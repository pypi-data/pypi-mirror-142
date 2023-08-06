from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mrange:
	"""Mrange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mrange", core, parent)

	def set(self, range_py: enums.PowerVectorErrorMode) -> None:
		"""SCPI: CONFigure:WLAN:PVERror:MRANge \n
		Snippet: driver.applications.k91Wlan.configure.wlan.pvError.mrange.set(range_py = enums.PowerVectorErrorMode.ALL) \n
		This remote control command defines or queries whether the Peak Vector Error results are calculated over the complete
		PPDU or just over the PSDU. This command is supported for 802.11b and 802.11g (DSSS) only. \n
			:param range_py: ALL | PSDU ALL Peak Vector Error results are calculated over the complete PPDU PSDU Peak Vector Error results are calculated over the PSDU only
		"""
		param = Conversions.enum_scalar_to_str(range_py, enums.PowerVectorErrorMode)
		self._core.io.write(f'CONFigure:WLAN:PVERror:MRANge {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerVectorErrorMode:
		"""SCPI: CONFigure:WLAN:PVERror:MRANge \n
		Snippet: value: enums.PowerVectorErrorMode = driver.applications.k91Wlan.configure.wlan.pvError.mrange.get() \n
		This remote control command defines or queries whether the Peak Vector Error results are calculated over the complete
		PPDU or just over the PSDU. This command is supported for 802.11b and 802.11g (DSSS) only. \n
			:return: range_py: ALL | PSDU ALL Peak Vector Error results are calculated over the complete PPDU PSDU Peak Vector Error results are calculated over the PSDU only"""
		response = self._core.io.query_str(f'CONFigure:WLAN:PVERror:MRANge?')
		return Conversions.str_to_scalar_enum(response, enums.PowerVectorErrorMode)
