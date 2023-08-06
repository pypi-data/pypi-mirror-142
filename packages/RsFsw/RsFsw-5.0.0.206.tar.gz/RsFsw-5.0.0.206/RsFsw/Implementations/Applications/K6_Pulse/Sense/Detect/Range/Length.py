from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, detection_start: float) -> None:
		"""SCPI: [SENSe]:DETect:RANGe:LENGth \n
		Snippet: driver.applications.k6Pulse.sense.detect.range.length.set(detection_start = 1.0) \n
		Defines the length of the detection range as a time in seconds. This command is only available for [SENSe:]DETect:RANGe
		ON. \n
			:param detection_start: Unit: S
		"""
		param = Conversions.decimal_value_to_str(detection_start)
		self._core.io.write(f'SENSe:DETect:RANGe:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:RANGe:LENGth \n
		Snippet: value: float = driver.applications.k6Pulse.sense.detect.range.length.get() \n
		Defines the length of the detection range as a time in seconds. This command is only available for [SENSe:]DETect:RANGe
		ON. \n
			:return: detection_start: No help available"""
		response = self._core.io.query_str(f'SENSe:DETect:RANGe:LENGth?')
		return Conversions.str_to_float(response)
