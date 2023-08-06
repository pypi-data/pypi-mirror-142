from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	def set(self, count: float) -> None:
		"""SCPI: CONFigure:DDPD:COUNt \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.count.set(count = 1.0) \n
		This command defines the number of iterations in a direct DPD sequence.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param count: numeric value (integer only) Range: 1 to 1000
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'CONFigure:DDPD:COUNt {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DDPD:COUNt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.ddpd.count.get() \n
		This command defines the number of iterations in a direct DPD sequence.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: count: numeric value (integer only) Range: 1 to 1000"""
		response = self._core.io.query_str(f'CONFigure:DDPD:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
