from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:TRACking:PHASe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.tracking.phase.set(state = False) \n
		This command turns phase tracking on and off. \n
			:param state: OFF Deactivate phase tracking PIL Pilot only Corresponds to ON for PRACH analysis PILPAY Pilot and payload Unavailable for PRACH analysis.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:TRACking:PHASe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:TRACking:PHASe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.tracking.phase.get() \n
		This command turns phase tracking on and off. \n
			:return: state: OFF Deactivate phase tracking PIL Pilot only Corresponds to ON for PRACH analysis PILPAY Pilot and payload Unavailable for PRACH analysis."""
		response = self._core.io.query_str(f'SENSe:NR5G:TRACking:PHASe?')
		return Conversions.str_to_bool(response)
