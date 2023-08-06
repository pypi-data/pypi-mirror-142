from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace_number: float) -> None:
		"""SCPI: [SENSe]:POWer:TRACe \n
		Snippet: driver.sense.power.trace.set(trace_number = 1.0) \n
		This command selects the trace channel power measurements are performed on. For the measurement to work,
		the corresponding trace has to be active. \n
			:param trace_number: Range: 1 to 6
		"""
		param = Conversions.decimal_value_to_str(trace_number)
		self._core.io.write(f'SENSe:POWer:TRACe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:TRACe \n
		Snippet: value: float = driver.sense.power.trace.get() \n
		This command selects the trace channel power measurements are performed on. For the measurement to work,
		the corresponding trace has to be active. \n
			:return: trace_number: Range: 1 to 6"""
		response = self._core.io.query_str(f'SENSe:POWer:TRACe?')
		return Conversions.str_to_float(response)
