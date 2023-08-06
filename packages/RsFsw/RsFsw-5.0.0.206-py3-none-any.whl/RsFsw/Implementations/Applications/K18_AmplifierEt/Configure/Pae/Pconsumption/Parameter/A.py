from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class A:
	"""A commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("a", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: CONFigure:PAE:PCONsumption[:PARameter]:A \n
		Snippet: driver.applications.k18AmplifierEt.configure.pae.pconsumption.parameter.a.set(value = 1.0) \n
		No command help available \n
			:param value: No help available
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:PAE:PCONsumption:PARameter:A {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PAE:PCONsumption[:PARameter]:A \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.pae.pconsumption.parameter.a.get() \n
		No command help available \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'CONFigure:PAE:PCONsumption:PARameter:A?')
		return Conversions.str_to_float(response)
