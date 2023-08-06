from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Euids:
	"""Euids commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("euids", core, parent)

	def set(self, ids: str, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:EUIDs \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.euids.set(ids = '1', carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines user IDs that are excluded from the calculation of modulation-specific EVM results. \n
			:param ids: String containg the user IDs to exclude. This is either a comma-separated list (1,2,5,6) , a range (1-6) or a combination of both.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(ids)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:EUIDs {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:EUIDs \n
		Snippet: value: str = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.euids.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines user IDs that are excluded from the calculation of modulation-specific EVM results. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: ids: String containg the user IDs to exclude. This is either a comma-separated list (1,2,5,6) , a range (1-6) or a combination of both."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:EUIDs?')
		return trim_str_response(response)
