from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:TIME \n
		Snippet: driver.applications.k91Wlan.sense.tracking.time.set(state = False) \n
		Activates or deactivates the compensation for timing drift. If activated, the measurement results are compensated for
		timing error on a per-symbol basis. For details see 'Tracking the phase drift, timing jitter and gain'. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:TIME {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:TIME \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.tracking.time.get() \n
		Activates or deactivates the compensation for timing drift. If activated, the measurement results are compensated for
		timing error on a per-symbol basis. For details see 'Tracking the phase drift, timing jitter and gain'. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:TRACking:TIME?')
		return Conversions.str_to_bool(response)
