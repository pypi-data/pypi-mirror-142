from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slot:
	"""Slot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slot", core, parent)

	def set(self, slot: float) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:SLOT \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.slot.set(slot = 1.0) \n
		This command defines the number of slots that are analyzed. \n
			:param slot: ALL Analyzes all slots in a frame. numeric value (integer only) Analyzes a certain number of slots in a frame.
		"""
		param = Conversions.decimal_value_to_str(slot)
		self._core.io.write(f'SENSe:NR5G:FRAMe:SLOT {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:FRAMe:SLOT \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.frame.slot.get() \n
		This command defines the number of slots that are analyzed. \n
			:return: slot: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:SLOT?')
		return Conversions.str_to_float(response)
