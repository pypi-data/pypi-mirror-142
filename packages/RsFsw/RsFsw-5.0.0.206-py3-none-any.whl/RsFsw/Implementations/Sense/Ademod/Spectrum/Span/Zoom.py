from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zoom:
	"""Zoom commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zoom", core, parent)

	def set(self, span: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN:ZOOM \n
		Snippet: driver.sense.ademod.spectrum.span.zoom.set(span = 1.0) \n
		This command sets the span (around the center frequency) for RF spectrum result display. The span is limited to the
		demodulation bandwidth (see [SENSe:]BWIDth:DEMod) . \n
			:param span: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(span)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:SPAN:ZOOM {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN:ZOOM \n
		Snippet: value: float = driver.sense.ademod.spectrum.span.zoom.get() \n
		This command sets the span (around the center frequency) for RF spectrum result display. The span is limited to the
		demodulation bandwidth (see [SENSe:]BWIDth:DEMod) . \n
			:return: span: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:SPAN:ZOOM?')
		return Conversions.str_to_float(response)
