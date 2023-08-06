from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McFilter:
	"""McFilter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcFilter", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:MCFilter \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.mcFilter.set(state = False) \n
		This command turns the multicarrier filter during demodulation on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:DEMod:MCFilter {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:DEMod:MCFilter \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.demod.mcFilter.get() \n
		This command turns the multicarrier filter during demodulation on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:MCFilter?')
		return Conversions.str_to_bool(response)
