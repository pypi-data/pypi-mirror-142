from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self) -> bool:
		"""SCPI: [SENSe]:SUBSpan:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.subspan.state.get() \n
		Queries the state of the frequency subspan measurements. This can be helpful when using subspan mode 'Auto' where the R&S
		FSW-K17S decides automatically if subspan measurements are active (query state 'ON') or inactive (query state 'OFF') . \n
			:return: state: ON | OFF"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:STATe?')
		return Conversions.str_to_bool(response)
