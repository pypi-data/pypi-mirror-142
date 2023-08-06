from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Events:
	"""Events commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("events", core, parent)

	def set(self, count: int) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: driver.sense.sweep.scapture.events.set(count = 1) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:SWEep:SCAPture:EVENts {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: value: int = driver.sense.sweep.scapture.events.get() \n
		No command help available \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:EVENts?')
		return Conversions.str_to_int(response)
