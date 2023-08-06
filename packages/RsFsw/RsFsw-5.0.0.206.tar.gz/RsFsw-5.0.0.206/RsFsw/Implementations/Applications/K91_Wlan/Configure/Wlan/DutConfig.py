from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutConfig:
	"""DutConfig commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutConfig", core, parent)

	def set(self, no_of_ant: enums.AntennasCount) -> None:
		"""SCPI: CONFigure:WLAN:DUTConfig \n
		Snippet: driver.applications.k91Wlan.configure.wlan.dutConfig.set(no_of_ant = enums.AntennasCount.TX1) \n
		This remote control command specifies the number of antennas used for MIMO measurement. \n
			:param no_of_ant: TX1 | TX2 | TX3 | TX4 | TX5 | TX6 | TX7 | TX8 TX1: one antenna, TX2: two antennas etc.
		"""
		param = Conversions.enum_scalar_to_str(no_of_ant, enums.AntennasCount)
		self._core.io.write(f'CONFigure:WLAN:DUTConfig {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AntennasCount:
		"""SCPI: CONFigure:WLAN:DUTConfig \n
		Snippet: value: enums.AntennasCount = driver.applications.k91Wlan.configure.wlan.dutConfig.get() \n
		This remote control command specifies the number of antennas used for MIMO measurement. \n
			:return: no_of_ant: TX1 | TX2 | TX3 | TX4 | TX5 | TX6 | TX7 | TX8 TX1: one antenna, TX2: two antennas etc."""
		response = self._core.io.query_str(f'CONFigure:WLAN:DUTConfig?')
		return Conversions.str_to_scalar_enum(response, enums.AntennasCount)
