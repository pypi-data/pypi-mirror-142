from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Span:
	"""Span commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	@property
	def full(self):
		"""full commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_full'):
			from .Full import Full
			self._full = Full(self._core, self._cmd_group)
		return self._full

	def set(self, span: float) -> None:
		"""SCPI: [SENSe]:FREQuency:SPAN \n
		Snippet: driver.sense.frequency.span.set(span = 1.0) \n
		This command defines the frequency span. If you set a span of 0 Hz in the Spectrum application, the R&S FSW starts a
		measurement in the time domain. \n
			:param span: The minimum span for measurements in the frequency domain is 10 Hz. For SEM and spurious emission measurements, the minimum span is 20 Hz. Range: 0 Hz to fmax, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(span)
		self._core.io.write(f'SENSe:FREQuency:SPAN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:SPAN \n
		Snippet: value: float = driver.sense.frequency.span.get() \n
		This command defines the frequency span. If you set a span of 0 Hz in the Spectrum application, the R&S FSW starts a
		measurement in the time domain. \n
			:return: span: The minimum span for measurements in the frequency domain is 10 Hz. For SEM and spurious emission measurements, the minimum span is 20 Hz. Range: 0 Hz to fmax, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:SPAN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Span':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Span(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
