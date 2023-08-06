from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmethod:
	"""Cmethod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmethod", core, parent)

	def set(self, state: enums.EvmCalcState) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CMEThod \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.cmethod.set(state = enums.EvmCalcState.AOTP) \n
		This command selects the EVM calculation method. \n
			:param state: HPOS EVM at high timing position LPOS EVM at low timing position OTP EVM at optimal timing position TGPP EVM according to 3GPP definition
		"""
		param = Conversions.enum_scalar_to_str(state, enums.EvmCalcState)
		self._core.io.write(f'SENSe:NR5G:DEMod:CMEThod {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EvmCalcState:
		"""SCPI: [SENSe]:NR5G:DEMod:CMEThod \n
		Snippet: value: enums.EvmCalcState = driver.applications.k14Xnr5G.sense.nr5G.demod.cmethod.get() \n
		This command selects the EVM calculation method. \n
			:return: state: HPOS EVM at high timing position LPOS EVM at low timing position OTP EVM at optimal timing position TGPP EVM according to 3GPP definition"""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CMEThod?')
		return Conversions.str_to_scalar_enum(response, enums.EvmCalcState)
