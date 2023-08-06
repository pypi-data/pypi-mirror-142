from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, no_of_antennas: enums.NoOfMimoAntennas, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MIMO:CONFig \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mimo.config.set(no_of_antennas = enums.NoOfMimoAntennas.TX1, carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the number of antennas in the MIMO setup. \n
			:param no_of_antennas: TX1 Use one Tx-antenna TX2 Use two Tx-antennas TX4 Use four Tx-antennas
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(no_of_antennas, enums.NoOfMimoAntennas)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MIMO:CONFig {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.NoOfMimoAntennas:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MIMO:CONFig \n
		Snippet: value: enums.NoOfMimoAntennas = driver.applications.k10Xlte.configure.lte.downlink.cc.mimo.config.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the number of antennas in the MIMO setup. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: no_of_antennas: TX1 Use one Tx-antenna TX2 Use two Tx-antennas TX4 Use four Tx-antennas"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MIMO:CONFig?')
		return Conversions.str_to_scalar_enum(response, enums.NoOfMimoAntennas)
