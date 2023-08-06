from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutLimit:
	"""DutLimit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutLimit", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.level.dutLimit.set(value = 1.0) \n
		This command defines the output power RMS level of the generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) .
			- DUT peak input power limit is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Level.DutLimit.State.set) . \n
			:param value: Unit: dB
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:GENerator:LEVel:DUTLimit {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.generator.level.dutLimit.get() \n
		This command defines the output power RMS level of the generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) .
			- DUT peak input power limit is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Level.DutLimit.State.set) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:LEVel:DUTLimit?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DutLimit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DutLimit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
