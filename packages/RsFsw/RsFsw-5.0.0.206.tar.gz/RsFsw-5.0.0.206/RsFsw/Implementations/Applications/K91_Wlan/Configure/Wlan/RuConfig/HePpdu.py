from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HePpdu:
	"""HePpdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hePpdu", core, parent)

	def set(self, ru_config_ppdu: enums.RuConfigPpdu) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:HEPPdu \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.hePpdu.set(ru_config_ppdu = enums.RuConfigPpdu.ESU) \n
		Defines the format of the HE PPDU. This format determines which other PPDU settings are available. \n
			:param ru_config_ppdu: SU | MU | TRIG | ESU SU High-efficiency single user PPDU for uplink and downlink MU High-efficiency multi-user PPDU for downlink to multiple users at the same time TRIG High-efficiency trigger-based PPDU for uplink from multiple users at the same time ESU High-efficiency single-user PPDU for an extended range
		"""
		param = Conversions.enum_scalar_to_str(ru_config_ppdu, enums.RuConfigPpdu)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:HEPPdu {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RuConfigPpdu:
		"""SCPI: CONFigure:WLAN:RUConfig:HEPPdu \n
		Snippet: value: enums.RuConfigPpdu = driver.applications.k91Wlan.configure.wlan.ruConfig.hePpdu.get() \n
		Defines the format of the HE PPDU. This format determines which other PPDU settings are available. \n
			:return: ru_config_ppdu: SU | MU | TRIG | ESU SU High-efficiency single user PPDU for uplink and downlink MU High-efficiency multi-user PPDU for downlink to multiple users at the same time TRIG High-efficiency trigger-based PPDU for uplink from multiple users at the same time ESU High-efficiency single-user PPDU for an extended range"""
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:HEPPdu?')
		return Conversions.str_to_scalar_enum(response, enums.RuConfigPpdu)
