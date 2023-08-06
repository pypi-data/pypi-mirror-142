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
		"""SCPI: [SENSe]:BWIDth[:RESolution]:RATio \n
		Snippet: driver.sense.bandwidth.resolution.ratio.set(ratio = 1.0) \n
		This command defines the ratio between the resolution bandwidth (Hz) and the span (Hz) . Note that the ratio defined with
		this remote command (RBW/span) is reciprocal to that of the coupling ratio (span/RBW) . \n
			:param ratio: Range: 0.0001 to 1
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SENSe:BWIDth:RESolution:RATio {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:RATio \n
		Snippet: value: float = driver.sense.bandwidth.resolution.ratio.get() \n
		This command defines the ratio between the resolution bandwidth (Hz) and the span (Hz) . Note that the ratio defined with
		this remote command (RBW/span) is reciprocal to that of the coupling ratio (span/RBW) . \n
			:return: ratio: Range: 0.0001 to 1"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:RATio?')
		return Conversions.str_to_float(response)
