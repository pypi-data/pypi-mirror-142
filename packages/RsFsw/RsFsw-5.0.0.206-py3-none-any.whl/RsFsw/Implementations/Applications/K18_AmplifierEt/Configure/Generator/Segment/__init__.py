from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, segment: float) -> None:
		"""SCPI: CONFigure:GENerator:SEGMent \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.segment.set(segment = 1.0) \n
		This command selects the segment in a multi-waveform file that should be selected on the signal generator. Make sure to
		synchronize with *OPC? or *WAI to make sure that the command was successfully applied on the generator before sending the
		next command. \n
			:param segment: numeric value: (integer only) Range: Depends on the number of segments in the waveform file.
		"""
		param = Conversions.decimal_value_to_str(segment)
		self._core.io.write(f'CONFigure:GENerator:SEGMent {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:SEGMent \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.segment.get() \n
		This command selects the segment in a multi-waveform file that should be selected on the signal generator. Make sure to
		synchronize with *OPC? or *WAI to make sure that the command was successfully applied on the generator before sending the
		next command. \n
			:return: segment: numeric value: (integer only) Range: Depends on the number of segments in the waveform file."""
		response = self._core.io.query_str(f'CONFigure:GENerator:SEGMent?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
