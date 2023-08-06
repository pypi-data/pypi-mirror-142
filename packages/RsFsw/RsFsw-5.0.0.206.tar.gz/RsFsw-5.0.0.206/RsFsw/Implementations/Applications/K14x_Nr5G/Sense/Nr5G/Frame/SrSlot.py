from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrSlot:
	"""SrSlot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srSlot", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:SRSLot \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.srSlot.set(state = False) \n
		This command turns analysis of custom signals with repeating slots on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:FRAMe:SRSLot {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:FRAMe:SRSLot \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.frame.srSlot.get() \n
		This command turns analysis of custom signals with repeating slots on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:SRSLot?')
		return Conversions.str_to_bool(response)
