from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Omode:
	"""Omode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("omode", core, parent)

	def set(self, mode: enums.FreqOffsetMode) -> None:
		"""SCPI: CONFigure[:NR5G]:OMODe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.omode.set(mode = enums.FreqOffsetMode.ARBitrary) \n
		This command selects the frequency offset mode for component carriers in a multicarrier setup. \n
			:param mode: ARBitrary Distance between component carriers is arbitrary. You can define the frequency offsets with [SENSe:]FREQuency:CENTer[:CCcc]:OFFSet. EQUidistant Component carriers have the same distance between each other. You can define the spacing between carriers with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Cspacing.set.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqOffsetMode)
		self._core.io.write(f'CONFigure:NR5G:OMODe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FreqOffsetMode:
		"""SCPI: CONFigure[:NR5G]:OMODe \n
		Snippet: value: enums.FreqOffsetMode = driver.applications.k14Xnr5G.configure.nr5G.omode.get() \n
		This command selects the frequency offset mode for component carriers in a multicarrier setup. \n
			:return: mode: ARBitrary Distance between component carriers is arbitrary. You can define the frequency offsets with [SENSe:]FREQuency:CENTer[:CCcc]:OFFSet. EQUidistant Component carriers have the same distance between each other. You can define the spacing between carriers with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Cspacing.set."""
		response = self._core.io.query_str(f'CONFigure:NR5G:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.FreqOffsetMode)
