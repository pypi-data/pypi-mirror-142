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

	def set(self, state: bool, inputIx=repcap.InputIx.Default, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:SLISt<sli>:STATe \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.slist.state.set(state = False, inputIx = repcap.InputIx.Default, touchStone = repcap.TouchStone.Default) \n
		Activates or deactivates the loaded file for the current configuration. Only active files are included in filter
		calculation. For queries with no input type specified, the currently active input type is queried. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Activates the file. ON | 1 Deactivates the file.
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:SLISt{touchStone_cmd_val}:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default, touchStone=repcap.TouchStone.Default) -> bool:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:SLISt<sli>:STATe \n
		Snippet: value: bool = driver.sense.correction.fresponse.inputPy.user.slist.state.get(inputIx = repcap.InputIx.Default, touchStone = repcap.TouchStone.Default) \n
		Activates or deactivates the loaded file for the current configuration. Only active files are included in filter
		calculation. For queries with no input type specified, the currently active input type is queried. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Activates the file. ON | 1 Deactivates the file."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:SLISt{touchStone_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
