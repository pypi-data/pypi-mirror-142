from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LastSpan:
	"""LastSpan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lastSpan", core, parent)

	def set(self, last_span: float) -> None:
		"""SCPI: [SENSe]:SUBSpan:LASTspan \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.lastSpan.set(last_span = 1.0) \n
		No command help available \n
			:param last_span: No help available
		"""
		param = Conversions.decimal_value_to_str(last_span)
		self._core.io.write(f'SENSe:SUBSpan:LASTspan {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan:LASTspan \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.lastSpan.get() \n
		No command help available \n
			:return: last_span: No help available"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:LASTspan?')
		return Conversions.str_to_float(response)
