from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	def set(self, arbc_lock_freq: float) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:ARBitrary:CLOCk \n
		Snippet: driver.configure.generator.npratio.bb.arbitrary.clock.set(arbc_lock_freq = 1.0) \n
		No command help available \n
			:param arbc_lock_freq: No help available
		"""
		param = Conversions.decimal_value_to_str(arbc_lock_freq)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:BB:ARBitrary:CLOCk {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:BB:ARBitrary:CLOCk \n
		Snippet: value: float = driver.configure.generator.npratio.bb.arbitrary.clock.get() \n
		No command help available \n
			:return: arbc_lock_freq: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:BB:ARBitrary:CLOCk?')
		return Conversions.str_to_float(response)
