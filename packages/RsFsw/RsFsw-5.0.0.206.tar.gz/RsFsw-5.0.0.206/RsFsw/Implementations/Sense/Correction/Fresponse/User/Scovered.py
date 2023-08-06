from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scovered:
	"""Scovered commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scovered", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SCOVered \n
		Snippet: value: float = driver.sense.correction.fresponse.user.scovered.get() \n
		Indicates whether the frequency correction file covers the full measurement span. \n
			:return: covered: 0 | 1 0 Span not fully covered 1 Full measurement span is covered"""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:SCOVered?')
		return Conversions.str_to_float(response)
