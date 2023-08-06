from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uers:
	"""Uers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uers", core, parent)

	def set(self, port: enums.AntennaPortA, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP[:UERS] \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.uers.set(port = enums.AntennaPortA.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param port: Antenna port used by the UE reference signal. ALL Shows the results for all antenna ports. AP_5_7 | AP_8 | AP_9 | AP_10 | AP_11 | AP_12 | AP_13 | AP_14 Shows the results for antenna port 5/7, 8, 9, 10, 11, 12, 13 or 14 only.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(port, enums.AntennaPortA)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:UERS {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaPortA:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP[:UERS] \n
		Snippet: value: enums.AntennaPortA = driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.uers.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: port: Antenna port used by the UE reference signal. ALL Shows the results for all antenna ports. AP_5_7 | AP_8 | AP_9 | AP_10 | AP_11 | AP_12 | AP_13 | AP_14 Shows the results for antenna port 5/7, 8, 9, 10, 11, 12, 13 or 14 only."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:UERS?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPortA)
