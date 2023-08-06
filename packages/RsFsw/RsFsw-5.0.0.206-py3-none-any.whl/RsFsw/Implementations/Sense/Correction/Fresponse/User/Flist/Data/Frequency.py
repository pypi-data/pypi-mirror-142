from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get(self, fileList=repcap.FileList.Default) -> float:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:DATA:FREQuency \n
		Snippet: value: float = driver.sense.correction.fresponse.user.flist.data.frequency.get(fileList = repcap.FileList.Default) \n
		Queries the trace values for the selected .fres file. \n
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: result: No help available"""
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:DATA:FREQuency?')
		return Conversions.str_to_float(response)
