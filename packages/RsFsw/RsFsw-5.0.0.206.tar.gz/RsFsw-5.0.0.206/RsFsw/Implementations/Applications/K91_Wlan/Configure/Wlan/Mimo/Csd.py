from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csd:
	"""Csd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csd", core, parent)

	def set(self, method: enums.CsdSyncMethod) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:CSD \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.csd.set(method = enums.CsdSyncMethod.APPLy) \n
		Determines whether or not the cyclic shift delay (CSD) is used for timing synchronisation. \n
			:param method: IGNore | APPLy APPLy (Default:) The timing offset estimation result (assuming CSD=0) is used for the subsequent signal analysis. IGNore The timing offset estimation result (assuming CSD=0) is ignored for the subsequent signal analysis.
		"""
		param = Conversions.enum_scalar_to_str(method, enums.CsdSyncMethod)
		self._core.io.write(f'CONFigure:WLAN:MIMO:CSD {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CsdSyncMethod:
		"""SCPI: CONFigure:WLAN:MIMO:CSD \n
		Snippet: value: enums.CsdSyncMethod = driver.applications.k91Wlan.configure.wlan.mimo.csd.get() \n
		Determines whether or not the cyclic shift delay (CSD) is used for timing synchronisation. \n
			:return: method: IGNore | APPLy APPLy (Default:) The timing offset estimation result (assuming CSD=0) is used for the subsequent signal analysis. IGNore The timing offset estimation result (assuming CSD=0) is ignored for the subsequent signal analysis."""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:CSD?')
		return Conversions.str_to_scalar_enum(response, enums.CsdSyncMethod)
