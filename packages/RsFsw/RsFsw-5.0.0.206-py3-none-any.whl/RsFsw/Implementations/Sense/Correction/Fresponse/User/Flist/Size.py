from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Size:
	"""Size commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("size", core, parent)

	def get(self, fileList=repcap.FileList.Default) -> int:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:SIZE \n
		Snippet: value: int = driver.sense.correction.fresponse.user.flist.size.get(fileList = repcap.FileList.Default) \n
		Queries the number of entries in the list of .fres files for the current configuration. \n
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: size: integer Range: 1 to 15"""
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:SIZE?')
		return Conversions.str_to_int(response)
