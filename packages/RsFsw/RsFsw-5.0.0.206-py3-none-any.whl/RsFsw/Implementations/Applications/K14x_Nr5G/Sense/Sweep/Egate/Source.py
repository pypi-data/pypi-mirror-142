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

	def set(self, source: enums.GatedSourceNr5G) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.source.set(source = enums.GatedSourceNr5G.EXT2) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.GatedSourceNr5G)
		self._core.io.write(f'SENSe:SWEep:EGATe:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GatedSourceNr5G:
		"""SCPI: [SENSe]:SWEep:EGATe:SOURce \n
		Snippet: value: enums.GatedSourceNr5G = driver.applications.k14Xnr5G.sense.sweep.egate.source.get() \n
		No command help available \n
			:return: source: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.GatedSourceNr5G)
