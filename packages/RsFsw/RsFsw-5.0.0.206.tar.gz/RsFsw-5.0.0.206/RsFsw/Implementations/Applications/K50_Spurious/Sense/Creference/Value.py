from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, max_peak: float) -> None:
		"""SCPI: [SENSe]:CREFerence:VALue \n
		Snippet: driver.applications.k50Spurious.sense.creference.value.set(max_peak = 1.0) \n
		Defines the maximum peak of the signal, which is considered to be the reference carrier. \n
			:param max_peak: Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(max_peak)
		self._core.io.write(f'SENSe:CREFerence:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CREFerence:VALue \n
		Snippet: value: float = driver.applications.k50Spurious.sense.creference.value.get() \n
		Defines the maximum peak of the signal, which is considered to be the reference carrier. \n
			:return: max_peak: Unit: DBM"""
		response = self._core.io.query_str(f'SENSe:CREFerence:VALue?')
		return Conversions.str_to_float(response)
