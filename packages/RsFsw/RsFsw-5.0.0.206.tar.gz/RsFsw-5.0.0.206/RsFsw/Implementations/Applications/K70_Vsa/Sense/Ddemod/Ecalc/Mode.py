from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, evm_calc: enums.EvmCalc) -> None:
		"""SCPI: [SENSe]:DDEMod:ECALc[:MODE] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.ecalc.mode.set(evm_calc = enums.EvmCalc.MACPower) \n
		This command defines the calculation formula for EVM. \n
			:param evm_calc: SIGNal | SYMBol | MECPower | MACPower SIGNal Calculation normalized to the mean power of the reference signal at the symbol instants. SYMBol Calculation normalized to the maximum power of the reference signal at the symbol instants. MECPower Calculation normalized to the mean expected power of the measurement signal at the symbol instants MACPower Calculation normalized to the maximum expected power of the measurement signal at the symbol instants
		"""
		param = Conversions.enum_scalar_to_str(evm_calc, enums.EvmCalc)
		self._core.io.write(f'SENSe:DDEMod:ECALc:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EvmCalc:
		"""SCPI: [SENSe]:DDEMod:ECALc[:MODE] \n
		Snippet: value: enums.EvmCalc = driver.applications.k70Vsa.sense.ddemod.ecalc.mode.get() \n
		This command defines the calculation formula for EVM. \n
			:return: evm_calc: SIGNal | SYMBol | MECPower | MACPower SIGNal Calculation normalized to the mean power of the reference signal at the symbol instants. SYMBol Calculation normalized to the maximum power of the reference signal at the symbol instants. MECPower Calculation normalized to the mean expected power of the measurement signal at the symbol instants MACPower Calculation normalized to the maximum expected power of the measurement signal at the symbol instants"""
		response = self._core.io.query_str(f'SENSe:DDEMod:ECALc:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvmCalc)
