from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfFrequency:
	"""IfFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifFrequency", core, parent)

	def set(self, arg_0: float, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<ou>:IF:IFFRequency \n
		Snippet: driver.applications.k6Pulse.output.ifreq.ifFrequency.set(arg_0 = 1.0, outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:IFFRequency {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> float:
		"""SCPI: OUTPut<ou>:IF:IFFRequency \n
		Snippet: value: float = driver.applications.k6Pulse.output.ifreq.ifFrequency.get(outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: arg_0: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:IFFRequency?')
		return Conversions.str_to_float(response)
