from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Falling:
	"""Falling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("falling", core, parent)

	def set(self, run_out: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:SKIP:FALLing \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.skip.falling.set(run_out = 1.0) \n
		This command defines the length of the falling burst edge which is not considered when evaluating the result. \n
			:param run_out: Range: 1 , Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(run_out)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:SKIP:FALLing {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:SKIP:FALLing \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.skip.falling.get() \n
		This command defines the length of the falling burst edge which is not considered when evaluating the result. \n
			:return: run_out: Range: 1 , Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:SKIP:FALLing?')
		return Conversions.str_to_float(response)
