from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:SWEep:TIME \n
		Snippet: driver.sense.sweep.time.set(time = 1.0) \n
		This command defines the sweep time. It automatically decouples the time from any other settings. In the Spectrum
		application, the command decouples the sweep time from the span and resolution and video bandwidths. Note that this
		command queries only the time required to capture the data, not to process it. To obtain an estimation of the total
		capture and processing time, use the [SENSe:]SWEep:DURation? command. \n
			:param time: refer to data sheet Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:SWEep:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:TIME \n
		Snippet: value: float = driver.sense.sweep.time.get() \n
		This command defines the sweep time. It automatically decouples the time from any other settings. In the Spectrum
		application, the command decouples the sweep time from the span and resolution and video bandwidths. Note that this
		command queries only the time required to capture the data, not to process it. To obtain an estimation of the total
		capture and processing time, use the [SENSe:]SWEep:DURation? command. \n
			:return: time: refer to data sheet Unit: S"""
		response = self._core.io.query_str(f'SENSe:SWEep:TIME?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Time':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Time(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
