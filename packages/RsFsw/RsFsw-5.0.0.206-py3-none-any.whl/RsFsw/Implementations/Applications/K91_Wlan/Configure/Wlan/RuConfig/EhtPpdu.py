from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EhtPpdu:
	"""EhtPpdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ehtPpdu", core, parent)

	def set(self, ru_config_ppdu: enums.RuConfigPpdu) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:EHTPpdu \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.ehtPpdu.set(ru_config_ppdu = enums.RuConfigPpdu.ESU) \n
		Defines the format of the EHT PPDU. This format determines which other PPDU settings are available. \n
			:param ru_config_ppdu: MU High-efficiency multi-user PPDU for downlink to multiple users at the same time
		"""
		param = Conversions.enum_scalar_to_str(ru_config_ppdu, enums.RuConfigPpdu)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:EHTPpdu {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RuConfigPpdu:
		"""SCPI: CONFigure:WLAN:RUConfig:EHTPpdu \n
		Snippet: value: enums.RuConfigPpdu = driver.applications.k91Wlan.configure.wlan.ruConfig.ehtPpdu.get() \n
		Defines the format of the EHT PPDU. This format determines which other PPDU settings are available. \n
			:return: ru_config_ppdu: MU High-efficiency multi-user PPDU for downlink to multiple users at the same time"""
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:EHTPpdu?')
		return Conversions.str_to_scalar_enum(response, enums.RuConfigPpdu)
