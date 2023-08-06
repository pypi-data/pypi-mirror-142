from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EflRange:
	"""EflRange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eflRange", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:EFLRange \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.eflRange.set(state = False) \n
		This command turns the extended frequency lock range on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:DEMod:EFLRange {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:DEMod:EFLRange \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.demod.eflRange.get() \n
		This command turns the extended frequency lock range on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:EFLRange?')
		return Conversions.str_to_bool(response)
