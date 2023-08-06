from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Active:
	"""Active commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> str:
		"""SCPI: [SENSe]:CORRection:TRANsducer:INPut<ip>:ACTive \n
		Snippet: value: str = driver.sense.correction.transducer.inputPy.active.get(inputIx = repcap.InputIx.Default) \n
		No command help available \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: transducer_factor: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'SENSe:CORRection:TRANsducer:INPut{inputIx_cmd_val}:ACTive?')
		return trim_str_response(response)
