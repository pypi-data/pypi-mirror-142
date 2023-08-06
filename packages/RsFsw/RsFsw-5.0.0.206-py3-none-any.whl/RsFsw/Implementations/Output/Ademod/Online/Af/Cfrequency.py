from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfrequency:
	"""Cfrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfrequency", core, parent)

	def set(self, frequency: float, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:AF[:CFRequency] \n
		Snippet: driver.output.ademod.online.af.cfrequency.set(frequency = 1.0, outputConnector = repcap.OutputConnector.Default) \n
		This command defines the cutoff frequency for the AC highpass filter (for AC coupling only,
		see [SENSe:]ADEMod<n>:AF:COUPling) . \n
			:param frequency: numeric value Range: 10 Hz to DemodBW/10 (= 300 kHz for active demodulation output) , Unit: HZ
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:AF:CFRequency {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> float:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:AF[:CFRequency] \n
		Snippet: value: float = driver.output.ademod.online.af.cfrequency.get(outputConnector = repcap.OutputConnector.Default) \n
		This command defines the cutoff frequency for the AC highpass filter (for AC coupling only,
		see [SENSe:]ADEMod<n>:AF:COUPling) . \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: frequency: numeric value Range: 10 Hz to DemodBW/10 (= 300 kHz for active demodulation output) , Unit: HZ"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:AF:CFRequency?')
		return Conversions.str_to_float(response)
