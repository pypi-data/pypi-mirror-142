from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def set(self, hysteresis: float) -> None:
		"""SCPI: [SENSe]:DETect:HYSTeresis \n
		Snippet: driver.applications.k6Pulse.sense.detect.hysteresis.set(hysteresis = 1.0) \n
		Defines a hysteresis for pulse detection in dB in relation to the defined threshold (see [SENSe:]DETect:THReshold) .
		As long as the signal does not exceed the hysteresis, the next threshold crossing is ignored. \n
			:param hysteresis: Unit: DB
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		self._core.io.write(f'SENSe:DETect:HYSTeresis {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DETect:HYSTeresis \n
		Snippet: value: float = driver.applications.k6Pulse.sense.detect.hysteresis.get() \n
		Defines a hysteresis for pulse detection in dB in relation to the defined threshold (see [SENSe:]DETect:THReshold) .
		As long as the signal does not exceed the hysteresis, the next threshold crossing is ignored. \n
			:return: hysteresis: Unit: DB"""
		response = self._core.io.query_str(f'SENSe:DETect:HYSTeresis?')
		return Conversions.str_to_float(response)
