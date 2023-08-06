from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, repetition_count: float) -> None:
		"""SCPI: TRACe:IQ:FILE:REPetition:COUNt \n
		Snippet: driver.trace.iq.file.repetition.count.set(repetition_count = 1.0) \n
		Determines how often the data stream is repeatedly copied in the I/Q data memory. If the available memory is not
		sufficient for the specified number of repetitions, the largest possible number of complete data streams is used. \n
			:param repetition_count: integer
		"""
		param = Conversions.decimal_value_to_str(repetition_count)
		self._core.io.write(f'TRACe:IQ:FILE:REPetition:COUNt {param}')

	def get(self) -> float:
		"""SCPI: TRACe:IQ:FILE:REPetition:COUNt \n
		Snippet: value: float = driver.trace.iq.file.repetition.count.get() \n
		Determines how often the data stream is repeatedly copied in the I/Q data memory. If the available memory is not
		sufficient for the specified number of repetitions, the largest possible number of complete data streams is used. \n
			:return: repetition_count: integer"""
		response = self._core.io.query_str(f'TRACe:IQ:FILE:REPetition:COUNt?')
		return Conversions.str_to_float(response)
