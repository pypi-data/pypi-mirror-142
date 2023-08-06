from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:MIXer:THReshold \n
		Snippet: driver.applications.k14Xnr5G.sense.mixer.threshold.set(value = 1.0) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:MIXer:THReshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:THReshold \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.mixer.threshold.get() \n
		No command help available \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:THReshold?')
		return Conversions.str_to_float(response)
