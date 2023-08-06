from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtime:
	"""Mtime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtime", core, parent)

	def set(self, meas_time: float) -> None:
		"""SCPI: [SENSe]:MTIMe \n
		Snippet: driver.applications.k60Transient.sense.mtime.set(meas_time = 1.0) \n
		This command defines the time data is captured. Note that the record length and the measurement time are interdependent
		(see [SENSe:]RLENgth) . \n
			:param meas_time: Range: 18.75 us to 1.298 ms, Unit: S
		"""
		param = Conversions.decimal_value_to_str(meas_time)
		self._core.io.write(f'SENSe:MTIMe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MTIMe \n
		Snippet: value: float = driver.applications.k60Transient.sense.mtime.get() \n
		This command defines the time data is captured. Note that the record length and the measurement time are interdependent
		(see [SENSe:]RLENgth) . \n
			:return: meas_time: Range: 18.75 us to 1.298 ms, Unit: S"""
		response = self._core.io.query_str(f'SENSe:MTIMe?')
		return Conversions.str_to_float(response)
