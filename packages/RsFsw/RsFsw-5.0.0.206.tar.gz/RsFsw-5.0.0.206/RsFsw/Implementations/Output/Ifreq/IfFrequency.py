from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfFrequency:
	"""IfFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifFrequency", core, parent)

	def set(self, frequency: float, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:IF:IFFRequency \n
		Snippet: driver.output.ifreq.ifFrequency.set(frequency = 1.0, outputConnector = repcap.OutputConnector.Default) \n
		This command defines the frequency for the IF output of the R&S FSW. The IF frequency of the signal is converted
		accordingly. This command is available in the time domain and if the IF/VIDEO/DEMOD output is configured for IF. If the
		[IF WIDE OUTPUT] connector is used (TRACe:IQ:WBANd ON, see method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set) ,
		this command is available as a query only. It returns the used IF output frequency which is defined automatically by the
		application according to the center frequency. For more information see 'IF and video signal output'. \n
			:param frequency: Unit: HZ
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:IFFRequency {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> float:
		"""SCPI: OUTPut<up>:IF:IFFRequency \n
		Snippet: value: float = driver.output.ifreq.ifFrequency.get(outputConnector = repcap.OutputConnector.Default) \n
		This command defines the frequency for the IF output of the R&S FSW. The IF frequency of the signal is converted
		accordingly. This command is available in the time domain and if the IF/VIDEO/DEMOD output is configured for IF. If the
		[IF WIDE OUTPUT] connector is used (TRACe:IQ:WBANd ON, see method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.State.set) ,
		this command is available as a query only. It returns the used IF output frequency which is defined automatically by the
		application according to the center frequency. For more information see 'IF and video signal output'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: frequency: Unit: HZ"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:IFFRequency?')
		return Conversions.str_to_float(response)
