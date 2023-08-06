from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rising:
	"""Rising commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rising", core, parent)

	def set(self, run_in: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:SKIP:RISing \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.skip.rising.set(run_in = 1.0) \n
		No command help available \n
			:param run_in: Range: 0 to 31990, Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(run_in)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:SKIP:RISing {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:SKIP:RISing \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.skip.rising.get() \n
		No command help available \n
			:return: run_in: Range: 0 to 31990, Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:SKIP:RISing?')
		return Conversions.str_to_float(response)
