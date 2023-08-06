from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Samples:
	"""Samples commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("samples", core, parent)

	def get(self) -> int:
		"""SCPI: [SENSe]:DDEMod:SEARch:MBURst:STARt:SAMPles \n
		Snippet: value: int = driver.applications.k70Vsa.sense.ddemod.search.mburst.start.samples.get() \n
		This command queries the start sample of the current result range within the capture buffer. Tip: to query the start
		symbol, use [SENSe:]DDEMod:SEARch:MBURst:STARt[:SYMBols]?. \n
			:return: start: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:MBURst:STARt:SAMPles?')
		return Conversions.str_to_int(response)
