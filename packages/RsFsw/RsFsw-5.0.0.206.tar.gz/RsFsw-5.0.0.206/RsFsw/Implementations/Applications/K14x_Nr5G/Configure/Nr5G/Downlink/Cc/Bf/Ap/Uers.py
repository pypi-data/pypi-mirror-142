from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uers:
	"""Uers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uers", core, parent)

	def set(self, port: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:BF:AP[:UERS] \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.bf.ap.uers.set(port = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects an antenna port to analyze. \n
			:param port: ALL Selects all antenna ports. numeric_value (integer only) Selects a specific antenna port. The value corresponds to the antenna port number.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(port)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:BF:AP:UERS {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:BF:AP[:UERS] \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.bf.ap.uers.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects an antenna port to analyze. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: port: ALL Selects all antenna ports. numeric_value (integer only) Selects a specific antenna port. The value corresponds to the antenna port number."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:BF:AP:UERS?')
		return Conversions.str_to_float(response)
