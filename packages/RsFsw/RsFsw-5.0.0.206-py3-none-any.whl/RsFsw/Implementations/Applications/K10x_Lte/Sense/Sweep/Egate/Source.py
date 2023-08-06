from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.GatedSourceLte) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: driver.applications.k10Xlte.sense.sweep.egate.source.set(source = enums.GatedSourceLte.EXT2) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.GatedSourceLte)
		self._core.io.write(f'SENSe:SWEep:EGATe:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GatedSourceLte:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: value: enums.GatedSourceLte = driver.applications.k10Xlte.sense.sweep.egate.source.get() \n
		No command help available \n
			:return: source: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.GatedSourceLte)
