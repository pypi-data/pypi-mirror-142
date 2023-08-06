from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtime:
	"""Dtime commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtime", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:SWEep:DTIMe \n
		Snippet: driver.sense.sweep.dtime.set(time = 1.0) \n
		Determines the amount of time used to sample a continuous stream of I/Q data. The stream is displayed as multiple rows in
		the spectrogram or waterfall diagrams (as opposed to the sweep time, which defines the time to capture a single row in
		the diagrams) . Dwell time is never applied for triggered measurements. It is only applied in single sweep mode or when
		the Sequencer is in continuous mode. The query returns the amount of time used to sample I/Q data in the current
		measurement. Tip: the dwell time can also be defined automatically, see [SENSe:]SWEep:DTIMe:AUTO. For more information
		see 'Sweep time and detector'. \n
			:param time: numeric value Range: 30 ms to 3600 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:SWEep:DTIMe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:DTIMe \n
		Snippet: value: float = driver.sense.sweep.dtime.get() \n
		Determines the amount of time used to sample a continuous stream of I/Q data. The stream is displayed as multiple rows in
		the spectrogram or waterfall diagrams (as opposed to the sweep time, which defines the time to capture a single row in
		the diagrams) . Dwell time is never applied for triggered measurements. It is only applied in single sweep mode or when
		the Sequencer is in continuous mode. The query returns the amount of time used to sample I/Q data in the current
		measurement. Tip: the dwell time can also be defined automatically, see [SENSe:]SWEep:DTIMe:AUTO. For more information
		see 'Sweep time and detector'. \n
			:return: time: numeric value Range: 30 ms to 3600 s, Unit: s"""
		response = self._core.io.query_str(f'SENSe:SWEep:DTIMe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Dtime':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dtime(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
