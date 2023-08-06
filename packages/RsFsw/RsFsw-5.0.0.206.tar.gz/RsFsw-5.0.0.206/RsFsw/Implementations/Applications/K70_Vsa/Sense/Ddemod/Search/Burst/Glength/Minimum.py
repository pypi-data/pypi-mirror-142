from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, min_gap_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:GLENgth[:MINimum] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.glength.minimum.set(min_gap_length = 1.0) \n
		This command defines the minimum time between two bursts. A minimum time with decreased level must occur between two
		bursts. The default unit is symbol. The value can also be given in seconds. \n
			:param min_gap_length: Range: 1 to 15000, Unit: SYM
		"""
		param = Conversions.decimal_value_to_str(min_gap_length)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:GLENgth:MINimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:GLENgth[:MINimum] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.glength.minimum.get() \n
		This command defines the minimum time between two bursts. A minimum time with decreased level must occur between two
		bursts. The default unit is symbol. The value can also be given in seconds. \n
			:return: min_gap_length: Range: 1 to 15000, Unit: SYM"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:GLENgth:MINimum?')
		return Conversions.str_to_float(response)
