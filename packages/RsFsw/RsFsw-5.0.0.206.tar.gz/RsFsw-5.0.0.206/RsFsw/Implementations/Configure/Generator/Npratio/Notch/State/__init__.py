from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


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

	def set(self, state: bool, notch=repcap.Notch.Default) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:NOTCh<notch>[:STATe] \n
		Snippet: driver.configure.generator.npratio.notch.state.set(state = False, notch = repcap.Notch.Default) \n
		Enables or disables the specified notch on the signal generator. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The notch is not considered for signal generation on the connected signal generator. ON | 1 The notch is considered for signal generation on the connected signal generator.
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.bool_to_str(state)
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:NOTCh{notch_cmd_val}:STATe {param}')

	def get(self, notch=repcap.Notch.Default) -> bool:
		"""SCPI: CONFigure:GENerator:NPRatio:NOTCh<notch>[:STATe] \n
		Snippet: value: bool = driver.configure.generator.npratio.notch.state.get(notch = repcap.Notch.Default) \n
		Enables or disables the specified notch on the signal generator. \n
			:param notch: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: state: ON | OFF | 0 | 1 OFF | 0 The notch is not considered for signal generation on the connected signal generator. ON | 1 The notch is considered for signal generation on the connected signal generator."""
		notch_cmd_val = self._cmd_group.get_repcap_cmd_value(notch, repcap.Notch)
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:NOTCh{notch_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
