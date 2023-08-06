from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	def set(self, port: enums.AntennaPortC, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP:CELL \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.cell.set(port = enums.AntennaPortC.ALL, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param port: Antenna port used by the cell reference signal. ALL Shows the results for all antenna ports. AP_0 | AP_1 | AP_2 | AP_3 Shows the results for antenna port 0, 1, 2 or 3 only.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(port, enums.AntennaPortC)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:CELL {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AntennaPortC:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:BF:AP:CELL \n
		Snippet: value: enums.AntennaPortC = driver.applications.k10Xlte.configure.lte.downlink.cc.bf.ap.cell.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the antenna port for which beamforming measurement results are displayed. The availabilty of ports
		depends on the number of transmit antennas and number of beamforming layers. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: port: Antenna port used by the cell reference signal. ALL Shows the results for all antenna ports. AP_0 | AP_1 | AP_2 | AP_3 Shows the results for antenna port 0, 1, 2 or 3 only."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:BF:AP:CELL?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaPortC)
