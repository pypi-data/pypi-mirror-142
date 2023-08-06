from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cvalue:
	"""Cvalue commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cvalue", core, parent)

	def set(self, user_compression: float) -> None:
		"""SCPI: CONFigure:CMEasurement:RESult:CVALue \n
		Snippet: driver.configure.cmeasurement.result.cvalue.set(user_compression = 1.0) \n
		No command help available \n
			:param user_compression: No help available
		"""
		param = Conversions.decimal_value_to_str(user_compression)
		self._core.io.write(f'CONFigure:CMEasurement:RESult:CVALue {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CMEasurement:RESult:CVALue \n
		Snippet: value: float = driver.configure.cmeasurement.result.cvalue.get() \n
		No command help available \n
			:return: user_compression: No help available"""
		response = self._core.io.query_str(f'CONFigure:CMEasurement:RESult:CVALue?')
		return Conversions.str_to_float(response)
