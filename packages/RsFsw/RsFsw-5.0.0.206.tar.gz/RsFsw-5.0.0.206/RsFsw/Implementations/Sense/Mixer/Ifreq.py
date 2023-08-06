from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ifreq:
	"""Ifreq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifreq", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:IF \n
		Snippet: value: float = driver.sense.mixer.ifreq.get() \n
		Queries the intermediate frequency currently used by the external mixer. \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:IF?')
		return Conversions.str_to_float(response)
