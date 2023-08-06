from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, fileList=repcap.FileList.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:MAGNitude[:STATe] \n
		Snippet: driver.sense.correction.fresponse.user.flist.magnitude.state.set(state = False, fileList = repcap.FileList.Default) \n
		Activates or deactivates the use of the correction data in the selected file for magnitude results. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Applies the data for magnitude results. ON | 1 Does not apply the data for magnitude results.
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		param = Conversions.bool_to_str(state)
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:MAGNitude:STATe {param}')

	def get(self, fileList=repcap.FileList.Default) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:FLISt<fli>:MAGNitude[:STATe] \n
		Snippet: value: bool = driver.sense.correction.fresponse.user.flist.magnitude.state.get(fileList = repcap.FileList.Default) \n
		Activates or deactivates the use of the correction data in the selected file for magnitude results. \n
			:param fileList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Applies the data for magnitude results. ON | 1 Does not apply the data for magnitude results."""
		fileList_cmd_val = self._cmd_group.get_repcap_cmd_value(fileList, repcap.FileList)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:FLISt{fileList_cmd_val}:MAGNitude:STATe?')
		return Conversions.str_to_bool(response)
