from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interval:
	"""Interval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interval", core, parent)

	def set(self, interval: str) -> None:
		"""SCPI: DIAGnostic:SERVice:CALibration:INTerval \n
		Snippet: driver.diagnostic.service.calibration.interval.set(interval = '1') \n
		This command queries the recommended calibration interval (ISO 8601 duration) . \n
			:param interval: String containing the recommended calibration interval.
		"""
		param = Conversions.value_to_quoted_str(interval)
		self._core.io.write(f'DIAGnostic:SERVice:CALibration:INTerval {param}')

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:CALibration:INTerval \n
		Snippet: value: str = driver.diagnostic.service.calibration.interval.get() \n
		This command queries the recommended calibration interval (ISO 8601 duration) . \n
			:return: interval: String containing the recommended calibration interval."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:CALibration:INTerval?')
		return trim_str_response(response)
