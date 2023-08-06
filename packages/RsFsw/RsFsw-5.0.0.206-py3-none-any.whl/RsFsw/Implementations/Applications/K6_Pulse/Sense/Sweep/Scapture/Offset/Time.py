from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:OFFSet[:TIME] \n
		Snippet: driver.applications.k6Pulse.sense.sweep.scapture.offset.time.set(time = 1.0) \n
		Defines an offset to the trigger event at which data capturing starts. For a negative offset, data capturing starts
		before the actual trigger event. \n
			:param time: Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:SWEep:SCAPture:OFFSet:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:OFFSet[:TIME] \n
		Snippet: value: float = driver.applications.k6Pulse.sense.sweep.scapture.offset.time.get() \n
		Defines an offset to the trigger event at which data capturing starts. For a negative offset, data capturing starts
		before the actual trigger event. \n
			:return: time: Unit: s"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:OFFSet:TIME?')
		return Conversions.str_to_float(response)
