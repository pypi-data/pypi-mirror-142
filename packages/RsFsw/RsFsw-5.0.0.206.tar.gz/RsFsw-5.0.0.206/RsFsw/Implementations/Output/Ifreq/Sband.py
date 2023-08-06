from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sband:
	"""Sband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sband", core, parent)

	def get(self, outputConnector=repcap.OutputConnector.Default) -> float:
		"""SCPI: OUTPut<up>:IF:SBANd \n
		Snippet: value: float = driver.output.ifreq.sband.get(outputConnector = repcap.OutputConnector.Default) \n
		This command queries the sideband provided at the 'IF OUT 2 GHz' connector compared to the sideband of the RF signal. The
		sideband depends on the current center frequency. This command is available only if the output is configured for IF2 (see
		method RsFsw.Output.Ifreq.Source.set) . For more information and prerequisites see 'IF and video signal output'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: side_band: NORMal The sideband at the output is identical to the RF signal. INVerted The sideband at the output is the inverted RF signal sideband."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:SBANd?')
		return Conversions.str_to_float(response)
