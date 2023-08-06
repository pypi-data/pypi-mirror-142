from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remove:
	"""Remove commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remove", core, parent)

	def set(self, touchStone=repcap.TouchStone.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:REMove \n
		Snippet: driver.sense.correction.fresponse.baseband.user.slist.remove.set(touchStone = repcap.TouchStone.Default) \n
		Removes the specified touchstone file from the list. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
		"""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		self._core.io.write(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:REMove')

	def set_with_opc(self, touchStone=repcap.TouchStone.Default, opc_timeout_ms: int = -1) -> None:
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		"""SCPI: [SENSe]:CORRection:FRESponse:BASeband:USER:SLISt<sli>:REMove \n
		Snippet: driver.sense.correction.fresponse.baseband.user.slist.remove.set_with_opc(touchStone = repcap.TouchStone.Default) \n
		Removes the specified touchstone file from the list. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:BASeband:USER:SLISt{touchStone_cmd_val}:REMove', opc_timeout_ms)
