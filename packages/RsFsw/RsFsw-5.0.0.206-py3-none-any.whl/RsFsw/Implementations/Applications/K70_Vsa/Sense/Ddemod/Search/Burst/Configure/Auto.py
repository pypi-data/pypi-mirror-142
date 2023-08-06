from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:CONFigure:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.burst.configure.auto.set(state = False) \n
		This command sets the search tolerance and the min gap length to their default values. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DDEMod:SEARch:BURSt:CONFigure:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DDEMod:SEARch:BURSt:CONFigure:AUTO \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.ddemod.search.burst.configure.auto.get() \n
		This command sets the search tolerance and the min gap length to their default values. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:BURSt:CONFigure:AUTO?')
		return Conversions.str_to_bool(response)
