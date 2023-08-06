from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ratio:
	"""Ratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ratio", core, parent)

	def set(self, ratio: float) -> None:
		"""SCPI: [SENSe]:BWIDth:VIDeo:RATio \n
		Snippet: driver.sense.bandwidth.video.ratio.set(ratio = 1.0) \n
		This command defines the coupling ratio of the video bandwidth to the resolution bandwidth (VBW/RBW) . \n
			:param ratio: Range: 0,001 to 1000
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SENSe:BWIDth:VIDeo:RATio {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth:VIDeo:RATio \n
		Snippet: value: float = driver.sense.bandwidth.video.ratio.get() \n
		This command defines the coupling ratio of the video bandwidth to the resolution bandwidth (VBW/RBW) . \n
			:return: ratio: Range: 0,001 to 1000"""
		response = self._core.io.query_str(f'SENSe:BWIDth:VIDeo:RATio?')
		return Conversions.str_to_float(response)
