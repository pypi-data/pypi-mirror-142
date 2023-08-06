from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Opdsch:
	"""Opdsch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("opdsch", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:OPDSch \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.opdsch.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns overwriting of PDSCH resource elements for UEs that do not consider the CSI reference signal on and
		off. \n
			:param state: ON | 1 The CSI reference signal overwrites PDSCH resource elements. OFF | 0 PDSCH resource elements remain.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:OPDSch {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:OPDSch \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.opdsch.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns overwriting of PDSCH resource elements for UEs that do not consider the CSI reference signal on and
		off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON | 1 The CSI reference signal overwrites PDSCH resource elements. OFF | 0 PDSCH resource elements remain."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:OPDSch?')
		return Conversions.str_to_bool(response)
