from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Annotation:
	"""Annotation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("annotation", core, parent)

	def set(self, mode: enums.AnnotationMode) -> None:
		"""SCPI: [SENSe]:FREQuency:ANNotation \n
		Snippet: driver.sense.frequency.annotation.set(mode = enums.AnnotationMode.CSPan) \n
		Switches the labelling of the y-axis for frequency-based result diagrams. The frequency range itself is not changed. This
		function is not available in all applications and measurements. \n
			:param mode: CSPan | SSTop CSPan span / center SSTop start / stop frequency
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AnnotationMode)
		self._core.io.write(f'SENSe:FREQuency:ANNotation {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AnnotationMode:
		"""SCPI: [SENSe]:FREQuency:ANNotation \n
		Snippet: value: enums.AnnotationMode = driver.sense.frequency.annotation.get() \n
		Switches the labelling of the y-axis for frequency-based result diagrams. The frequency range itself is not changed. This
		function is not available in all applications and measurements. \n
			:return: mode: CSPan | SSTop CSPan span / center SSTop start / stop frequency"""
		response = self._core.io.query_str(f'SENSe:FREQuency:ANNotation?')
		return Conversions.str_to_scalar_enum(response, enums.AnnotationMode)
