from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Polynomial:
	"""Polynomial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polynomial", core, parent)

	def set(self, degree: float) -> None:
		"""SCPI: CONFigure:BURSt:AM:AM:POLYnomial \n
		Snippet: driver.applications.k91Wlan.configure.burst.am.am.polynomial.set(degree = 1.0) \n
		This remote control command specifies the degree of the polynomial regression model used to determine the AM/AM result
		display. The resulting coefficients of the regression polynomial can be queried using the method RsFsw.Applications.
		K91_Wlan.Fetch.Burst.Am.Am.Coeficients.get_ command. \n
			:param degree: integer Range: 1 to 20
		"""
		param = Conversions.decimal_value_to_str(degree)
		self._core.io.write(f'CONFigure:BURSt:AM:AM:POLYnomial {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:BURSt:AM:AM:POLYnomial \n
		Snippet: value: float = driver.applications.k91Wlan.configure.burst.am.am.polynomial.get() \n
		This remote control command specifies the degree of the polynomial regression model used to determine the AM/AM result
		display. The resulting coefficients of the regression polynomial can be queried using the method RsFsw.Applications.
		K91_Wlan.Fetch.Burst.Am.Am.Coeficients.get_ command. \n
			:return: degree: integer Range: 1 to 20"""
		response = self._core.io.query_str(f'CONFigure:BURSt:AM:AM:POLYnomial?')
		return Conversions.str_to_float(response)
