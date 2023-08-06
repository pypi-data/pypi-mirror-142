from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:CFReduction[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.state.set(state = False) \n
		Enables the crest factor reduction calculation. \n
			:param state: 0 | 1 | OFF | ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:CFReduction:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CFReduction[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.cfReduction.state.get() \n
		Enables the crest factor reduction calculation. \n
			:return: state: 0 | 1 | OFF | ON"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
