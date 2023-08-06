from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, inputIx=repcap.InputIx.Default, touchStone=repcap.TouchStone.Default) -> str:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:SLISt<sli>:CATalog \n
		Snippet: value: str = driver.sense.correction.fresponse.inputPy.user.slist.catalog.get(inputIx = repcap.InputIx.Default, touchStone = repcap.TouchStone.Default) \n
		Returns a list of currently configured touchstone format files. Tip: to determine the currently selected file, use the
		[SENSe:]CORRection:FRESponse<si>:USER:SLISt<sli>:SELect query. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:return: file_list: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:SLISt{touchStone_cmd_val}:CATalog?')
		return trim_str_response(response)
