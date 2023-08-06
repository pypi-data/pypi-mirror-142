from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PartNumber:
	"""PartNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("partNumber", core, parent)

	def get(self, probe=repcap.Probe.Default) -> str:
		"""SCPI: [SENSe]:PROBe<p>:ID:PARTnumber \n
		Snippet: value: str = driver.applications.k70Vsa.sense.probe.id.partNumber.get(probe = repcap.Probe.Default) \n
		Queries the R&S part number of the probe. \n
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: part_number: 1..n Selects the connector: 1 = Baseband Input I 2 = Baseband Input Q 3 = RF"""
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:ID:PARTnumber?')
		return trim_str_response(response)
