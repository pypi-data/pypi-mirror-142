from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remove:
	"""Remove commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remove", core, parent)

	def set(self, inputIx=repcap.InputIx.Default, fileList=repcap.FileList.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:FLISt<fli>:REMove \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.flist.remove.set(inputIx = repcap.InputIx.Default, fileList = repcap.FileList.Default) \n
		Removes the selected frequency response (.fres) file from the current configuration. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:FLISt{fileList_cmd_val}:REMove')

	def set_with_opc(self, inputIx=repcap.InputIx.Default, fileList=repcap.FileList.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:FLISt<fli>:REMove \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.flist.remove.set_with_opc(inputIx = repcap.InputIx.Default, fileList = repcap.FileList.Default) \n
		Removes the selected frequency response (.fres) file from the current configuration. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:FLISt{fileList_cmd_val}:REMove', opc_timeout_ms)
