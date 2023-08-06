from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:POLYnomial:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.kdata.prbs.polynomial.auto.set(state = False) \n
		Determines the coefficients of the polynomial and thus the feedback positions for the PRBS algorithm. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The coefficients a0, ..., aN of the polynomial must be defined manually using [SENSe:]DDEMod:KDATa:PRBS:POLYnomial[:ORDer]. ON | 1 Polynomial is defined automatically according to the PRBS type specified by [SENSe:]DDEMod:KDATa:PRBS[:TYPE].
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:KDATa:PRBS:POLYnomial:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:KDATa:PRBS:POLYnomial:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.kdata.prbs.polynomial.auto.get() \n
		Determines the coefficients of the polynomial and thus the feedback positions for the PRBS algorithm. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The coefficients a0, ..., aN of the polynomial must be defined manually using [SENSe:]DDEMod:KDATa:PRBS:POLYnomial[:ORDer]. ON | 1 Polynomial is defined automatically according to the PRBS type specified by [SENSe:]DDEMod:KDATa:PRBS[:TYPE]."""
		response = self._core.io.query_str(f'SENSe:DDEMod:KDATa:PRBS:POLYnomial:AUTO?')
		return Conversions.str_to_bool(response)
