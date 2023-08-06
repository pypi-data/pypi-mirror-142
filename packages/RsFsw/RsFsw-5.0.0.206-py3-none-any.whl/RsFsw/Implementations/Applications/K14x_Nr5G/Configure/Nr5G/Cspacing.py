from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cspacing:
	"""Cspacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cspacing", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure[:NR5G]:CSPacing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.cspacing.set(frequency = 1.0) \n
		This command defines the carrier spacing for equidistant frequency offsets in a multicarrier setup. This frequency offset
		applies to all component carriers in the setup.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select equidistant frequency offset (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Omode.set) . \n
			:param frequency: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:NR5G:CSPacing {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:NR5G]:CSPacing \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.cspacing.get() \n
		This command defines the carrier spacing for equidistant frequency offsets in a multicarrier setup. This frequency offset
		applies to all component carriers in the setup.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select equidistant frequency offset (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Omode.set) . \n
			:return: frequency: Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:NR5G:CSPacing?')
		return Conversions.str_to_float(response)
