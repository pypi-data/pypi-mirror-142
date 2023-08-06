from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, symbol_rate: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SRATe \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.symbolRate.set(symbol_rate = 1.0) \n
		This command defines the symbol rate. The minimum symbol rate is 25 Hz. The maximum symbol rate depends on the defined
		'Sample Rate' (see 'Sample rate, symbol rate and I/Q bandwidth') . \n
			:param symbol_rate: Range: 25 to 250e6, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(symbol_rate)
		self._core.io.write(f'SENSe:DDEMod:SRATe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SRATe \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.symbolRate.get() \n
		This command defines the symbol rate. The minimum symbol rate is 25 Hz. The maximum symbol rate depends on the defined
		'Sample Rate' (see 'Sample rate, symbol rate and I/Q bandwidth') . \n
			:return: symbol_rate: Range: 25 to 250e6, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SRATe?')
		return Conversions.str_to_float(response)
