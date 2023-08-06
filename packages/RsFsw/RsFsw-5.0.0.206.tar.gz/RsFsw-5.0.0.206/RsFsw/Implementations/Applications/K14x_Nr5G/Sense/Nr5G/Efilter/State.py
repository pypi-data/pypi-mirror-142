from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:EFILter:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.efilter.state.set(state = False) \n
		This command turns an event filter for combined measurement results on and off. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:EFILter:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:EFILter:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.efilter.state.get() \n
		This command turns an event filter for combined measurement results on and off. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:NR5G:EFILter:STATe?')
		return Conversions.str_to_bool(response)
