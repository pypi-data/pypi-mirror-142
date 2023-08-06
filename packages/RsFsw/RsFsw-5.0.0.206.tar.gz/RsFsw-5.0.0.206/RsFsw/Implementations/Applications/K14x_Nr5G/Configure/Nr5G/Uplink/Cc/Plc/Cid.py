from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cid:
	"""Cid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cid", core, parent)

	def set(self, cell_id: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:CID \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.cid.set(cell_id = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the cell ID. \n
			:param cell_id: AUTO Automatically determines the cell ID. numeric value (integer only) Number of the cell ID. Range: 0 to 503
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(cell_id)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:CID {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PLC:CID \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.plc.cid.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the cell ID. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: cell_id: AUTO Automatically determines the cell ID. numeric value (integer only) Number of the cell ID. Range: 0 to 503"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PLC:CID?')
		return Conversions.str_to_float(response)
