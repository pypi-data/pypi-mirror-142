from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlength:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def set(self, sample_count: float) -> None:
		"""SCPI: [SENSe]:RLENgth \n
		Snippet: driver.applications.k60Transient.sense.rlength.set(sample_count = 1.0) \n
		This command defines the record length (in samples) for the current measurement. Note that the record length and the
		measurement time are interdependent (see [SENSe:]MTIMe) . \n
			:param sample_count: The maximum record length is limited only by the available memory.
		"""
		param = Conversions.decimal_value_to_str(sample_count)
		self._core.io.write(f'SENSe:RLENgth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:RLENgth \n
		Snippet: value: float = driver.applications.k60Transient.sense.rlength.get() \n
		This command defines the record length (in samples) for the current measurement. Note that the record length and the
		measurement time are interdependent (see [SENSe:]MTIMe) . \n
			:return: sample_count: The maximum record length is limited only by the available memory."""
		response = self._core.io.query_str(f'SENSe:RLENgth?')
		return Conversions.str_to_float(response)
