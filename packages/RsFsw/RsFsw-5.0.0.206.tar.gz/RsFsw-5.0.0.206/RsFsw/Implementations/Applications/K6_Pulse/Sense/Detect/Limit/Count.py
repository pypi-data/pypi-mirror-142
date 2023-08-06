from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, max_pulse_count: int) -> None:
		"""SCPI: [SENSe]:DETect:LIMit:COUNt \n
		Snippet: driver.applications.k6Pulse.sense.detect.limit.count.set(max_pulse_count = 1) \n
		Defines the maximum number of pulses to be detected. This limit is only considered if [SENSe:]DETect:LIMit is enabled. \n
			:param max_pulse_count: integer Range: 0 to see data sheet
		"""
		param = Conversions.decimal_value_to_str(max_pulse_count)
		self._core.io.write(f'SENSe:DETect:LIMit:COUNt {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:DETect:LIMit:COUNt \n
		Snippet: value: int = driver.applications.k6Pulse.sense.detect.limit.count.get() \n
		Defines the maximum number of pulses to be detected. This limit is only considered if [SENSe:]DETect:LIMit is enabled. \n
			:return: max_pulse_count: integer Range: 0 to see data sheet"""
		response = self._core.io.query_str(f'SENSe:DETect:LIMit:COUNt?')
		return Conversions.str_to_int(response)
