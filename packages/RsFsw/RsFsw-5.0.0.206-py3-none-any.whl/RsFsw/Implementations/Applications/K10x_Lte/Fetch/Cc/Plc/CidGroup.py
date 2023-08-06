from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CidGroup:
	"""CidGroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cidGroup", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh[:CC<cc>]:PLC:CIDGroup \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.cc.plc.cidGroup.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the cell identity group that has been detected. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: cid_group: The command returns -1 if no valid result has been detected yet. Range: 0 to 167"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:CC{carrierComponent_cmd_val}:PLC:CIDGroup?')
		return Conversions.str_to_float(response)
