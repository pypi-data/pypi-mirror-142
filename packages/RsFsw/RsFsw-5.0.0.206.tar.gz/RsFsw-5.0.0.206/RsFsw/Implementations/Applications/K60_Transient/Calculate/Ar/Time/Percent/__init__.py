from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Percent:
	"""Percent commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("percent", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, time_percent: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:AR:TIME:PERCent \n
		Snippet: driver.applications.k60Transient.calculate.ar.time.percent.set(time_percent = 1.0, window = repcap.Window.Default) \n
		For method RsFsw.Applications.K60_Transient.Calculate.Ar.Time.Percent.State.setTRUE,the length of the time gate, that is,
		the duration (or height) of the analysis region, is defined as a percentage of the full measurement time. The time gate
		start is the start of the capture buffer plus an offset defined by method RsFsw.Applications.K60_Transient.Calculate.Ar.
		Time.Start.set. \n
			:param time_percent: percentage of the full measurement time
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(time_percent)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:AR:TIME:PERCent {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:AR:TIME:PERCent \n
		Snippet: value: float = driver.applications.k60Transient.calculate.ar.time.percent.get(window = repcap.Window.Default) \n
		For method RsFsw.Applications.K60_Transient.Calculate.Ar.Time.Percent.State.setTRUE,the length of the time gate, that is,
		the duration (or height) of the analysis region, is defined as a percentage of the full measurement time. The time gate
		start is the start of the capture buffer plus an offset defined by method RsFsw.Applications.K60_Transient.Calculate.Ar.
		Time.Start.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: time_percent: percentage of the full measurement time"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:AR:TIME:PERCent?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Percent':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Percent(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
