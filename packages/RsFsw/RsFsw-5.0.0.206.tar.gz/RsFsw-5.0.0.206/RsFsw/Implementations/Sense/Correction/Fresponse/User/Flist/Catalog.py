from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, fileList=repcap.FileList.Default) -> str:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:CATalog \n
		Snippet: value: str = driver.sense.correction.fresponse.user.flist.catalog.get(fileList = repcap.FileList.Default) \n
		Returns a list of currently available .fres files in the directory. \n
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: file_list: No help available"""
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:CATalog?')
		return trim_str_response(response)
