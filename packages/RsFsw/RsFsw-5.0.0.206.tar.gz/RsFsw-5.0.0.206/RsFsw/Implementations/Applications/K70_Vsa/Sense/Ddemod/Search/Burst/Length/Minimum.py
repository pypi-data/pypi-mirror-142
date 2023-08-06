from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, useful_length: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:LENGth[:MINimum] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.length.minimum.set(useful_length = 1.0) \n
		This command defines the minimum useful length of a burst. Only those bursts will be recognized that exceed this length.
		The default unit is symbols. The value can also be given in seconds. Note the difference to manual operation:
		<Min_length>Manual= <Min_Useful_Length> + <Run-In> + <Run-Out> \n
			:param useful_length: numeric value Range: 10 to 32000, Unit: Sym
		"""
		param = Conversions.decimal_value_to_str(useful_length)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:LENGth:MINimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:LENGth[:MINimum] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.burst.length.minimum.get() \n
		This command defines the minimum useful length of a burst. Only those bursts will be recognized that exceed this length.
		The default unit is symbols. The value can also be given in seconds. Note the difference to manual operation:
		<Min_length>Manual= <Min_Useful_Length> + <Run-In> + <Run-Out> \n
			:return: useful_length: numeric value Range: 10 to 32000, Unit: Sym"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:LENGth:MINimum?')
		return Conversions.str_to_float(response)
