from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nap:
	"""Nap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def set(self, antenna_ports: enums.AntennaPortsLte, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:NAP \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.nap.set(antenna_ports = enums.AntennaPortsLte.TX1, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of antenna ports that transmit the CSI reference signal. \n
			:param antenna_ports: TX1 TX2 TX4 TX8
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(antenna_ports, enums.AntennaPortsLte)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:NAP {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaPortsLte:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:NAP \n
		Snippet: value: enums.AntennaPortsLte = driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.nap.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of antenna ports that transmit the CSI reference signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: antenna_ports: TX1 TX2 TX4 TX8"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPortsLte)
