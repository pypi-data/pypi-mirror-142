from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, segment_len: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: driver.sense.sweep.scapture.length.time.set(segment_len = 1.0) \n
		No command help available \n
			:param segment_len: No help available
		"""
		param = Conversions.decimal_value_to_str(segment_len)
		self._core.io.write(f'SENSe:SWEep:SCAPture:LENGth:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:LENGth[:TIME] \n
		Snippet: value: float = driver.sense.sweep.scapture.length.time.get() \n
		No command help available \n
			:return: segment_len: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:LENGth:TIME?')
		return Conversions.str_to_float(response)
