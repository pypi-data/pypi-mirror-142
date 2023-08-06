from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	def get(self) -> int:
		"""SCPI: [SENSe]:DDEMod:SEARch:MBURst:STARt[:SYMBols] \n
		Snippet: value: int = driver.applications.k70Vsa.sense.ddemod.search.mburst.start.symbols.get() \n
		This command queries the start symbol of the current result range within the capture buffer. Tip: to query the start
		sample, use [SENSe:]DDEMod:SEARch:MBURst:STARt:SAMPles?. \n
			:return: start: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:MBURst:STARt:SYMBols?')
		return Conversions.str_to_int(response)
