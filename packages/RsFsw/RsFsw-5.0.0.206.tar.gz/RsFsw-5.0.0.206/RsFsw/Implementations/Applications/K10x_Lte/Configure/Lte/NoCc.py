from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoCc:
	"""NoCc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noCc", core, parent)

	def set(self, carrier: float) -> None:
		"""SCPI: CONFigure[:LTE]:NOCC \n
		Snippet: driver.applications.k10Xlte.configure.lte.noCc.set(carrier = 1.0) \n
		This command selects the number of component carriers analyzed in the measurement. \n
			:param carrier: Number of the component carriers that you would like to measure. The range depends on the measurement. For more information see 'Carrier Aggregation'.
		"""
		param = Conversions.decimal_value_to_str(carrier)
		self._core.io.write(f'CONFigure:LTE:NOCC {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:NOCC \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.noCc.get() \n
		This command selects the number of component carriers analyzed in the measurement. \n
			:return: carrier: Number of the component carriers that you would like to measure. The range depends on the measurement. For more information see 'Carrier Aggregation'."""
		response = self._core.io.query_str(f'CONFigure:LTE:NOCC?')
		return Conversions.str_to_float(response)
