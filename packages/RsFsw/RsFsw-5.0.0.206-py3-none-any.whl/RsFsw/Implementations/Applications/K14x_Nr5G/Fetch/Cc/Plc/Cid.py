from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cid:
	"""Cid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cid", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh[:CC<cc>]:PLC:CID \n
		Snippet: value: float = driver.applications.k14Xnr5G.fetch.cc.plc.cid.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the cell ID. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: identity: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:CC{carrierComponent_cmd_val}:PLC:CID?')
		return Conversions.str_to_float(response)
