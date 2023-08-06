from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, freq_high: float) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH[:VALue] \n
		Snippet: driver.applications.k50Spurious.sense.mixer.harmonic.high.value.set(freq_high = 1.0) \n
		This command specifies the harmonic order to be used for the high (second) range. \n
			:param freq_high: 1..n irrelevant
		"""
		param = Conversions.decimal_value_to_str(freq_high)
		self._core.io.write(f'SENSe:MIXer:HARMonic:HIGH:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH[:VALue] \n
		Snippet: value: float = driver.applications.k50Spurious.sense.mixer.harmonic.high.value.get() \n
		This command specifies the harmonic order to be used for the high (second) range. \n
			:return: freq_high: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:HIGH:VALue?')
		return Conversions.str_to_float(response)
