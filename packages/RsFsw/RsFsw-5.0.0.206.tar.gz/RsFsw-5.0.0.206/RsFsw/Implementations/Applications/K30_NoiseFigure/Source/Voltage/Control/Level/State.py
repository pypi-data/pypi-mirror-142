from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, source=repcap.Source.Default) -> None:
		"""SCPI: SOURce:VOLTage:CONTrol<i>:LEVel[:STATe] \n
		Snippet: driver.applications.k30NoiseFigure.source.voltage.control.level.state.set(state = False, source = repcap.Source.Default) \n
		No command help available \n
			:param state: No help available
			:param source: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Control')
		"""
		param = Conversions.bool_to_str(state)
		source_cmd_val = self._cmd_group.get_repcap_cmd_value(source, repcap.Source)
		self._core.io.write(f'SOURce:VOLTage:CONTrol{source_cmd_val}:LEVel:STATe {param}')

	def get(self, source=repcap.Source.Default) -> bool:
		"""SCPI: SOURce:VOLTage:CONTrol<i>:LEVel[:STATe] \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.source.voltage.control.level.state.get(source = repcap.Source.Default) \n
		No command help available \n
			:param source: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Control')
			:return: state: No help available"""
		source_cmd_val = self._cmd_group.get_repcap_cmd_value(source, repcap.Source)
		response = self._core.io.query_str(f'SOURce:VOLTage:CONTrol{source_cmd_val}:LEVel:STATe?')
		return Conversions.str_to_bool(response)
