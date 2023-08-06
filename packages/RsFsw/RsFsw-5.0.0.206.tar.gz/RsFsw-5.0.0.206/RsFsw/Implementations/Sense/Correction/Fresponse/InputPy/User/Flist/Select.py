from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, file_path: str, inputIx=repcap.InputIx.Default, fileList=repcap.FileList.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:FLISt<fli>:SELect \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.flist.select.set(file_path = '1', inputIx = repcap.InputIx.Default, fileList = repcap.FileList.Default) \n
		Loads an additional frequency response (.fres) file to the current configuration. \n
			:param file_path: string Path and file name The default directory for .fres files is C:/R_S/INSTR/USER/Fresponse.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		param = Conversions.value_to_quoted_str(file_path)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:FLISt{fileList_cmd_val}:SELect {param}')
