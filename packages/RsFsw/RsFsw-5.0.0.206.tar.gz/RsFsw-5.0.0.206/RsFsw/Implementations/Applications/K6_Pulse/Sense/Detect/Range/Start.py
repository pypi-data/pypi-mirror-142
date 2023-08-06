from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, detection_start: float) -> None:
		"""SCPI: [SENSe]:DETect:RANGe:STARt \n
		Snippet: driver.applications.k6Pulse.sense.detect.range.start.set(detection_start = 1.0) \n
		Defines the beginning of the detection range as the time in seconds from the capture buffer start. This command is only
		available for [SENSe:]DETect:RANGe ON. \n
			:param detection_start: Time from the capture buffer start Unit: S
		"""
		param = Conversions.decimal_value_to_str(detection_start)
		self._core.io.write(f'SENSe:DETect:RANGe:STARt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:RANGe:STARt \n
		Snippet: value: float = driver.applications.k6Pulse.sense.detect.range.start.get() \n
		Defines the beginning of the detection range as the time in seconds from the capture buffer start. This command is only
		available for [SENSe:]DETect:RANGe ON. \n
			:return: detection_start: Time from the capture buffer start Unit: S"""
		response = self._core.io.query_str(f'SENSe:DETect:RANGe:STARt?')
		return Conversions.str_to_float(response)
