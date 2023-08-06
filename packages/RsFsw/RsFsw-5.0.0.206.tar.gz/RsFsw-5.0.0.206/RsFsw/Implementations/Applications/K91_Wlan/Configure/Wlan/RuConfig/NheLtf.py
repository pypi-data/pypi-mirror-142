from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NheLtf:
	"""NheLtf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nheLtf", core, parent)

	def set(self, ru_config_nhe_ltf: enums.RuConfigNheLtf) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:NHELtf \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.nheLtf.set(ru_config_nhe_ltf = enums.RuConfigNheLtf.S1) \n
		Defines the length of the high-efficiency long training field (for trigger-based uplink PPDUs only) .
		For more information see 'HE Trigger-based PPDUs'. \n
			:param ru_config_nhe_ltf: STA | S1 | S2 | S4 | S6 | S8 STA The station configuration defines the used length. S1 | S2 | S4 | S6 | S8 The LTF of the PPDUs have a fixed length (1 / 2 / 4 / 6 / 8 symbols) .
		"""
		param = Conversions.enum_scalar_to_str(ru_config_nhe_ltf, enums.RuConfigNheLtf)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:NHELtf {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RuConfigNheLtf:
		"""SCPI: CONFigure:WLAN:RUConfig:NHELtf \n
		Snippet: value: enums.RuConfigNheLtf = driver.applications.k91Wlan.configure.wlan.ruConfig.nheLtf.get() \n
		Defines the length of the high-efficiency long training field (for trigger-based uplink PPDUs only) .
		For more information see 'HE Trigger-based PPDUs'. \n
			:return: ru_config_nhe_ltf: STA | S1 | S2 | S4 | S6 | S8 STA The station configuration defines the used length. S1 | S2 | S4 | S6 | S8 The LTF of the PPDUs have a fixed length (1 / 2 / 4 / 6 / 8 symbols) ."""
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:NHELtf?')
		return Conversions.str_to_scalar_enum(response, enums.RuConfigNheLtf)
