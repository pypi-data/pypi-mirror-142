from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Min:
	"""Min commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("min", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:MIN \n
		Snippet: driver.applications.k9X11Ad.sense.demod.formatPy.banalyze.symbols.min.set(count = 1.0) \n
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:EQUal command has been set to true, then this command specifies the exact
		number of payload symbols a PPDU must have to take part in measurement analysis.
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:EQUal command is set to false, this command specifies the minimum number of
		payload symbols required for a PPDU to take part in measurement analysis. The number of payload symbols is defined as the
		uncoded bits including service and tail bits. \n
			:param count: integer
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:MIN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:MIN \n
		Snippet: value: float = driver.applications.k9X11Ad.sense.demod.formatPy.banalyze.symbols.min.get() \n
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:EQUal command has been set to true, then this command specifies the exact
		number of payload symbols a PPDU must have to take part in measurement analysis.
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:EQUal command is set to false, this command specifies the minimum number of
		payload symbols required for a PPDU to take part in measurement analysis. The number of payload symbols is defined as the
		uncoded bits including service and tail bits. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:MIN?')
		return Conversions.str_to_float(response)
