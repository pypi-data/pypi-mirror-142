from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpll:
	"""Dpll commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpll", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:IQ:DPLL \n
		Snippet: driver.applications.k40PhaseNoise.sense.iq.dpll.set(state = False) \n
		This command turns the digital PLL on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:IQ:DPLL {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:IQ:DPLL \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.iq.dpll.get() \n
		This command turns the digital PLL on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:IQ:DPLL?')
		return Conversions.str_to_bool(response)
