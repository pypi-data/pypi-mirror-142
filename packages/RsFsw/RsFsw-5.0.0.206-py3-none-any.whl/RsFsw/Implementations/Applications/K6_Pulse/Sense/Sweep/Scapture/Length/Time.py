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
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: driver.applications.k6Pulse.sense.sweep.scapture.length.time.set(time = 1.0) \n
		Defines a time period (starting from the trigger offset) in which data is captured. If multiple events occur within one
		segment length, the segment is extended (see 'Number of events vs number of segments') . \n
			:param time: Unit: s
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:SWEep:SCAPture:LENGth:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: value: float = driver.applications.k6Pulse.sense.sweep.scapture.length.time.get() \n
		Defines a time period (starting from the trigger offset) in which data is captured. If multiple events occur within one
		segment length, the segment is extended (see 'Number of events vs number of segments') . \n
			:return: time: Unit: s"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:LENGth:TIME?')
		return Conversions.str_to_float(response)
