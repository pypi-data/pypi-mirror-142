from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequencer:
	"""Sequencer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:SEQuencer \n
		Snippet: driver.system.sequencer.set(state = False) \n
		This command turns the Sequencer on and off. The Sequencer must be active before any other Sequencer commands (INIT:SEQ...
		) are executed, otherwise an error will occur. For details on the Sequencer see 'The Sequencer Concept'.
		A detailed programming example is provided in 'Programming Example: Performing a Sequence of Measurements'. \n
			:param state: ON | OFF | 0 | 1 ON | 1 The Sequencer is activated and a sequential measurement is started immediately. OFF | 0 The Sequencer is deactivated. Any running sequential measurements are stopped. Further Sequencer commands (INIT:SEQ...) are not available.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:SEQuencer {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:SEQuencer \n
		Snippet: value: bool = driver.system.sequencer.get() \n
		This command turns the Sequencer on and off. The Sequencer must be active before any other Sequencer commands (INIT:SEQ...
		) are executed, otherwise an error will occur. For details on the Sequencer see 'The Sequencer Concept'.
		A detailed programming example is provided in 'Programming Example: Performing a Sequence of Measurements'. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 The Sequencer is activated and a sequential measurement is started immediately. OFF | 0 The Sequencer is deactivated. Any running sequential measurements are stopped. Further Sequencer commands (INIT:SEQ...) are not available."""
		response = self._core.io.query_str(f'SYSTem:SEQuencer?')
		return Conversions.str_to_bool(response)
