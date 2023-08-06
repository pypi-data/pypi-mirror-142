from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvmCalc:
	"""EvmCalc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evmCalc", core, parent)

	def set(self, calculation: enums.CalculationLteEvm) -> None:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:EVMCalc \n
		Snippet: driver.applications.k10Xlte.sense.lte.downlink.demod.evmCalc.set(calculation = enums.CalculationLteEvm.OTP) \n
		This command selects the EVM calculation method. \n
			:param calculation: TGPP 3GPP definition OTP Optimal timing position
		"""
		param = Conversions.enum_scalar_to_str(calculation, enums.CalculationLteEvm)
		self._core.io.write(f'SENSe:LTE:DL:DEMod:EVMCalc {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CalculationLteEvm:
		"""SCPI: [SENSe][:LTE]:DL:DEMod:EVMCalc \n
		Snippet: value: enums.CalculationLteEvm = driver.applications.k10Xlte.sense.lte.downlink.demod.evmCalc.get() \n
		This command selects the EVM calculation method. \n
			:return: calculation: TGPP 3GPP definition OTP Optimal timing position"""
		response = self._core.io.query_str(f'SENSe:LTE:DL:DEMod:EVMCalc?')
		return Conversions.str_to_scalar_enum(response, enums.CalculationLteEvm)
