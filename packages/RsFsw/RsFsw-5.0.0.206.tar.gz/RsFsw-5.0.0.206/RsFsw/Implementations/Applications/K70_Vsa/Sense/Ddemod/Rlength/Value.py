from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, record_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:RLENgth[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.rlength.value.set(record_length = 1.0) \n
		This command defines or queries the capture length for further processing, e.g. for burst search. Note that the maximum
		capture length depends on the sample rate for signal capture (see [SENSe:]DDEMod:PRATe) . \n
			:param record_length: The capture length can be defined in time (seconds) or symbols (SYM) . The return value is always in time (s) . To query the capture length in symbols, use the [SENSe:]DDEMod:RLENgth:SYMBols[:VALue] command. Unit: S
		"""
		param = Conversions.decimal_value_to_str(record_length)
		self._core.io.write(f'SENSe:DDEMod:RLENgth:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:RLENgth[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.rlength.value.get() \n
		This command defines or queries the capture length for further processing, e.g. for burst search. Note that the maximum
		capture length depends on the sample rate for signal capture (see [SENSe:]DDEMod:PRATe) . \n
			:return: record_length: The capture length can be defined in time (seconds) or symbols (SYM) . The return value is always in time (s) . To query the capture length in symbols, use the [SENSe:]DDEMod:RLENgth:SYMBols[:VALue] command. Unit: S"""
		response = self._core.io.query_str(f'SENSe:DDEMod:RLENgth:VALue?')
		return Conversions.str_to_float(response)
