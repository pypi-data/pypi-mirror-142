from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	@property
	def link(self):
		"""link commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_link'):
			from .Link import Link
			self._link = Link(self._core, self._cmd_group)
		return self._link

	def set(self, frequency_step: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: driver.applications.k17Mcgd.sense.frequency.center.step.set(frequency_step = 1.0) \n
		This command defines the center frequency step size. You can increase or decrease the center frequency quickly in fixed
		steps using the SENS:FREQ UP AND SENS:FREQ DOWN commands, see [SENSe:]FREQuency:CENTer. \n
			:param frequency_step: fmax is specified in the data sheet. Range: 1 to fMAX, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency_step)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.frequency.center.step.get() \n
		This command defines the center frequency step size. You can increase or decrease the center frequency quickly in fixed
		steps using the SENS:FREQ UP AND SENS:FREQ DOWN commands, see [SENSe:]FREQuency:CENTer. \n
			:return: frequency_step: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Step':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Step(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
