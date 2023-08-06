from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spacing:
	"""Spacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spacing", core, parent)

	def set(self, carrier_spacing: float) -> None:
		"""SCPI: [SENSe]:ADEMod:MCPHase:SPACing \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.mcPhase.spacing.set(carrier_spacing = 1.0) \n
		Sets/queries the carrier spacing in Hz between the multiple carriers. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]CARRier:SPACing for new remote control programs. \n
			:param carrier_spacing: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(carrier_spacing)
		self._core.io.write(f'SENSe:ADEMod:MCPHase:SPACing {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:MCPHase:SPACing \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.mcPhase.spacing.get() \n
		Sets/queries the carrier spacing in Hz between the multiple carriers. Note that this command is maintained for
		compatibility reasons only. Use [SENSe:]CARRier:SPACing for new remote control programs. \n
			:return: carrier_spacing: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MCPHase:SPACing?')
		return Conversions.str_to_float(response)
