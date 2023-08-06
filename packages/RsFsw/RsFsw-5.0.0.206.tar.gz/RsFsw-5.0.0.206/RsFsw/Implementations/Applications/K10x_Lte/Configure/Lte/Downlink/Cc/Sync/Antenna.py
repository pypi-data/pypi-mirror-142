from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	def set(self, antenna: enums.AntennaB, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:ANTenna \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.sync.antenna.set(antenna = enums.AntennaB.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna that transmits the P-SYNC and the S-SYNC. \n
			:param antenna: ANT1 | ANT2 | ANT3 | ANT4 | ALL | NONE
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.AntennaB)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:ANTenna {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaB:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:ANTenna \n
		Snippet: value: enums.AntennaB = driver.applications.k10Xlte.configure.lte.downlink.cc.sync.antenna.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna that transmits the P-SYNC and the S-SYNC. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: antenna: ANT1 | ANT2 | ANT3 | ANT4 | ALL | NONE"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:ANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaB)
