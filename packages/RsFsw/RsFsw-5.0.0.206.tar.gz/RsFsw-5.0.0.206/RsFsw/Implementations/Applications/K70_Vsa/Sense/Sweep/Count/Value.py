from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, sweep_count: float) -> None:
		"""SCPI: [SENSe]:SWEep:COUNt[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.sweep.count.value.set(sweep_count = 1.0) \n
		No command help available \n
			:param sweep_count: No help available
		"""
		param = Conversions.decimal_value_to_str(sweep_count)
		self._core.io.write(f'SENSe:SWEep:COUNt:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.sweep.count.value.get() \n
		No command help available \n
			:return: sweep_count: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt:VALue?')
		return Conversions.str_to_float(response)
