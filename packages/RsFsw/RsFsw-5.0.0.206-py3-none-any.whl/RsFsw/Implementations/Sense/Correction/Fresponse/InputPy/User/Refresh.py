from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refresh:
	"""Refresh commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refresh", core, parent)

	def set(self, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:REFResh \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.refresh.set(inputIx = repcap.InputIx.Default) \n
		Recalculates the input source correction filter. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:REFResh')

	def set_with_opc(self, inputIx=repcap.InputIx.Default, opc_timeout_ms: int = -1) -> None:
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		"""SCPI: [SENSe]:CORRection:FRESponse:INPut<ip>:USER:REFResh \n
		Snippet: driver.sense.correction.fresponse.inputPy.user.refresh.set_with_opc(inputIx = repcap.InputIx.Default) \n
		Recalculates the input source correction filter. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CORRection:FRESponse:INPut{inputIx_cmd_val}:USER:REFResh', opc_timeout_ms)
