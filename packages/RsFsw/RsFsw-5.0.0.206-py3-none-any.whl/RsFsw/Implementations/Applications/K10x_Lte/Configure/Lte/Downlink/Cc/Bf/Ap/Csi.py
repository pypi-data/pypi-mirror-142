from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csi:
	"""Csi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csi", core, parent)

	def set(self, port: enums.AntennaPortB, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP:CSI \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.csi.set(port = enums.AntennaPortB.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param port: Antenna port used by the CSI reference signal. ALL Shows the results for all antenna ports. AP_15 | AP_16 | AP_17 | AP_18 | AP_19 | AP20 | AP21 | AP22 Shows the results for antenna port 15 to antenna port 22 only.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(port, enums.AntennaPortB)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:CSI {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaPortB:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP:CSI \n
		Snippet: value: enums.AntennaPortB = driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.csi.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: port: Antenna port used by the CSI reference signal. ALL Shows the results for all antenna ports. AP_15 | AP_16 | AP_17 | AP_18 | AP_19 | AP20 | AP21 | AP22 Shows the results for antenna port 15 to antenna port 22 only."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:CSI?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPortB)
