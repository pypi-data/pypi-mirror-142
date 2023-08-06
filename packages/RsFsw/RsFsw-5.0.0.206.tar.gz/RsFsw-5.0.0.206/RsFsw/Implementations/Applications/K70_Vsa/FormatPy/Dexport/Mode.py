from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.DataExportMode) -> None:
		"""SCPI: FORMat:DEXPort:MODE \n
		Snippet: driver.applications.k70Vsa.formatPy.dexport.mode.set(mode = enums.DataExportMode.RAW) \n
		This command defines which data are transferred, raw I/Q data or trace data. \n
			:param mode: RAW | TRACe
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DataExportMode)
		self._core.io.write(f'FORMat:DEXPort:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DataExportMode:
		"""SCPI: FORMat:DEXPort:MODE \n
		Snippet: value: enums.DataExportMode = driver.applications.k70Vsa.formatPy.dexport.mode.get() \n
		This command defines which data are transferred, raw I/Q data or trace data. \n
			:return: mode: RAW | TRACe"""
		response = self._core.io.query_str(f'FORMat:DEXPort:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.DataExportMode)
