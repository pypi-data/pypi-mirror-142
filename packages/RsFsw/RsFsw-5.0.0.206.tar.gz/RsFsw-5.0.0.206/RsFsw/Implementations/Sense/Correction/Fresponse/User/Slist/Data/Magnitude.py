from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Magnitude:
	"""Magnitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	def get(self, touchStone=repcap.TouchStone.Default, sPortPair=repcap.SPortPair.Ix1) -> float:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SLISt<sli>:DATA:MAGNitude<spi> \n
		Snippet: value: float = driver.sense.correction.fresponse.user.slist.data.magnitude.get(touchStone = repcap.TouchStone.Default, sPortPair = repcap.SPortPair.Ix1) \n
		Queries the trace values for the specified .snp file and ports. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:param sPortPair: optional repeated capability selector. Default value: Ix1
			:return: result: No help available"""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		sPortPair_cmd_val = self._cmd_group.get_repcap_cmd_value(sPortPair, repcap.SPortPair)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:SLISt{touchStone_cmd_val}:DATA:MAGNitude{sPortPair_cmd_val}?')
		return Conversions.str_to_float(response)
