from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Order:
	"""Order commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("order", core, parent)

	def set(self, prbs_poly_order: str) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:POLYnomial[:ORDer] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.polynomial.order.set(prbs_poly_order = '1') \n
		Determines the coefficients of the polynomial and thus the feedback positions for the PRBS algorithm. This function
		requires the R&S FSW-K70P option. \n
			:param prbs_poly_order: list of polynomial coefficents, separated by semi-colons (;) in descending order
		"""
		param = Conversions.value_to_quoted_str(prbs_poly_order)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:POLYnomial:ORDer {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:POLYnomial[:ORDer] \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.polynomial.order.get() \n
		Determines the coefficients of the polynomial and thus the feedback positions for the PRBS algorithm. This function
		requires the R&S FSW-K70P option. \n
			:return: prbs_poly_order: list of polynomial coefficents, separated by semi-colons (;) in descending order"""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:POLYnomial:ORDer?')
		return trim_str_response(response)
