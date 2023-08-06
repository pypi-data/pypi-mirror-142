from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)

	def set(self, segment: float) -> None:
		"""SCPI: CONFigure:REFSignal:SEGMent \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.segment.set(segment = 1.0) \n
		This command selects the segment of the reference signal that should be used in the measurement when the reference signal
		is based on a multi segment waveform file. \n
			:param segment: numeric value: (integer only) Range: Depends on the number of segments in the waveform file.
		"""
		param = Conversions.decimal_value_to_str(segment)
		self._core.io.write(f'CONFigure:REFSignal:SEGMent {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:SEGMent \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.segment.get() \n
		This command selects the segment of the reference signal that should be used in the measurement when the reference signal
		is based on a multi segment waveform file. \n
			:return: segment: numeric value: (integer only) Range: Depends on the number of segments in the waveform file."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:SEGMent?')
		return Conversions.str_to_float(response)
