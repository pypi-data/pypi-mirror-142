from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, max_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:LENGth:MAXimum \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.length.maximum.set(max_length = 1.0) \n
		No command help available \n
			:param max_length: Range: 0 to 128000, Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(max_length)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:LENGth:MAXimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:LENGth:MAXimum \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.length.maximum.get() \n
		No command help available \n
			:return: max_length: Range: 0 to 128000, Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:LENGth:MAXimum?')
		return Conversions.str_to_float(response)
