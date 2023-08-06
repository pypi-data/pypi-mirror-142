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

	def get(self, outputConnector=repcap.OutputConnector.Default) -> str:
		"""SCPI: OUTPut<up>:DIQ:CDEVice \n
		Snippet: value: str = driver.applications.k70Vsa.output.diq.cdevice.get(outputConnector = repcap.OutputConnector.Default) \n
		This command queries the current configuration and the status of the digital I/Q data output to the optional Digital
		Baseband Interface. For details see 'Interface Status Information'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: dig_iq_output_device_info: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:DIQ:CDEVice?')
		return trim_str_response(response)
