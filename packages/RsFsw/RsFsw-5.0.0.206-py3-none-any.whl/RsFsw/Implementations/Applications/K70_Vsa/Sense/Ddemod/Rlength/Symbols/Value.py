from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, record_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:RLENgth:SYMBols[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.rlength.symbols.value.set(record_length = 1.0) \n
		This command defines the capture length for further processing, e.g. for burst search, in symbols. Note that the maximum
		record length depends on the sample rate for signal capture (see [SENSe:]DDEMod:PRATe) . The maximum record length (in
		symbols) can be calculated as: RecordlengthMAX = 460000000/ <points per symbol> \n
			:param record_length: Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(record_length)
		self._core.io.write(f'SENSe:DDEMod:RLENgth:SYMBols:VALue {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:RLENgth:SYMBols[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.rlength.symbols.value.get() \n
		This command defines the capture length for further processing, e.g. for burst search, in symbols. Note that the maximum
		record length depends on the sample rate for signal capture (see [SENSe:]DDEMod:PRATe) . The maximum record length (in
		symbols) can be calculated as: RecordlengthMAX = 460000000/ <points per symbol> \n
			:return: record_length: Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:RLENgth:SYMBols:VALue?')
		return Conversions.str_to_float(response)
