from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get(self, outputConnector=repcap.OutputConnector.Default) -> float:
		"""SCPI: OUTPut<up>:IQHS:SRATe \n
		Snippet: value: float = driver.applications.k70Vsa.output.iqhs.symbolRate.get(outputConnector = repcap.OutputConnector.Default) \n
		Returns the currently used sample rate to transfer data via the Digital I/Q 40G Streaming Output interface. For details
		on Digital I/Q 40G Streaming Output (R&S FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: srate: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IQHS:SRATe?')
		return Conversions.str_to_float(response)
