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

	def set(self, source_file_prbs: enums.SourceFilePrbs) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:SOURce \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.source.set(source_file_prbs = enums.SourceFilePrbs.FILE) \n
		This command gets/selects the Known Data source \n
			:param source_file_prbs: FILE | PRBS
		"""
		param = Conversions.enum_scalar_to_str(source_file_prbs, enums.SourceFilePrbs)
		self._core.io.write(f'SENSe:DDEMod:KDATa:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceFilePrbs:
		"""SCPI: [SENSe]:DDEMod:KDATa:SOURce \n
		Snippet: value: enums.SourceFilePrbs = driver.applications.k70Vsa.sense.ddemod.kdata.source.get() \n
		This command gets/selects the Known Data source \n
			:return: source_file_prbs: FILE | PRBS"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceFilePrbs)
