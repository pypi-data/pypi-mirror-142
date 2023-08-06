from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, pretrigger: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:OFFSet[:TIME] \n
		Snippet: driver.sense.sweep.scapture.offset.time.set(pretrigger = 1.0) \n
		No command help available \n
			:param pretrigger: No help available
		"""
		param = Conversions.decimal_value_to_str(pretrigger)
		self._core.io.write(f'SENSe:SWEep:SCAPture:OFFSet:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:OFFSet[:TIME] \n
		Snippet: value: float = driver.sense.sweep.scapture.offset.time.get() \n
		No command help available \n
			:return: pretrigger: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:OFFSet:TIME?')
		return Conversions.str_to_float(response)
