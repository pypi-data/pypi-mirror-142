from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaMode:
	"""CaMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caMode", core, parent)

	def set(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:CAMode \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.caMode.set(mode = enums.AutoManualMode.AUTO) \n
		This command selects the CORESET analysis mode. \n
			:param mode: AUTO Automatic demodulation of the PDCCH. MANual Demodulation based on the PDCCH configuration.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'SENSe:NR5G:DEMod:CAMode {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:NR5G:DEMod:CAMode \n
		Snippet: value: enums.AutoManualMode = driver.applications.k14Xnr5G.sense.nr5G.demod.caMode.get() \n
		This command selects the CORESET analysis mode. \n
			:return: mode: AUTO Automatic demodulation of the PDCCH. MANual Demodulation based on the PDCCH configuration."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:CAMode?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
