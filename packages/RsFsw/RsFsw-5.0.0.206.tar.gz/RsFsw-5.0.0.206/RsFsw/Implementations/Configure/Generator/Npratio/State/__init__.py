from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def cstate(self):
		"""cstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstate'):
			from .Cstate import Cstate
			self._cstate = Cstate(self._core, self._cmd_group)
		return self._cstate

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio[:STATe] \n
		Snippet: driver.configure.generator.npratio.state.set(state = False) \n
		Activates or deactivates a notch filter on the signal generator. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:NPRatio[:STATe] \n
		Snippet: value: bool = driver.configure.generator.npratio.state.get() \n
		Activates or deactivates a notch filter on the signal generator. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
