from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdevice:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> str:
		"""SCPI: INPut<ip>:DIQ:CDEVice \n
		Snippet: value: str = driver.applications.k91Wlan.inputPy.diq.cdevice.get(inputIx = repcap.InputIx.Default) \n
		This command queries the current configuration and the status of the digital I/Q input from the optional Digital Baseband
		Interface. For details see 'Interface Status Information'. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: result: 1 | 2 irrelevant"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:DIQ:CDEVice?')
		return trim_str_response(response)
