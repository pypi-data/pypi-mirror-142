from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:MIXer:FREQuency:STARt \n
		Snippet: driver.applications.k40PhaseNoise.sense.mixer.frequency.start.set(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:MIXer:FREQuency:STARt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:FREQuency:STARt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.mixer.frequency.start.get() \n
		No command help available \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:FREQuency:STARt?')
		return Conversions.str_to_float(response)
