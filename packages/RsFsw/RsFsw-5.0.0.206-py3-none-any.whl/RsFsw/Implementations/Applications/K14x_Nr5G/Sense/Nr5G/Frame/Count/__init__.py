from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, frames: float) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.count.set(frames = 1.0) \n
		This command defines the number of frames to analyze.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on overall frame count ([SENSe:]NR5G:FRAMe:COUNt:STATe) . If the overall frame count is off, this command is a query only. \n
			:param frames: numeric value (integer only)
		"""
		param = Conversions.decimal_value_to_str(frames)
		self._core.io.write(f'SENSe:NR5G:FRAMe:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.frame.count.get() \n
		This command defines the number of frames to analyze.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on overall frame count ([SENSe:]NR5G:FRAMe:COUNt:STATe) . If the overall frame count is off, this command is a query only. \n
			:return: frames: numeric value (integer only)"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
