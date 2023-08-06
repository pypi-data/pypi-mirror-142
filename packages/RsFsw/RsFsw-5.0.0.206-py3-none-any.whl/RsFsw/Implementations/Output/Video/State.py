from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:VIDeo:STATe \n
		Snippet: driver.output.video.state.set(state = False, outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param state: No help available
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(state)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:VIDeo:STATe {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> bool:
		"""SCPI: OUTPut<up>:VIDeo:STATe \n
		Snippet: value: bool = driver.output.video.state.get(outputConnector = repcap.OutputConnector.Default) \n
		No command help available \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: state: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:VIDeo:STATe?')
		return Conversions.str_to_bool(response)
