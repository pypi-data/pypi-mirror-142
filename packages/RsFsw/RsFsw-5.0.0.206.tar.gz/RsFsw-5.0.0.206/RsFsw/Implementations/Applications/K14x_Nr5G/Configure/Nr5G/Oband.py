from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oband:
	"""Oband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oband", core, parent)

	def set(self, operating_band: enums.OperatingBandNr5G) -> None:
		"""SCPI: CONFigure[:NR5G]:OBANd \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.oband.set(operating_band = enums.OperatingBandNr5G.N1) \n
		This command selects the operating band.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select at least 2 component carriers (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) . \n
			:param operating_band: N1 | N2 | N3 | N5 | N7 | N8 | N12 | N14 | N18 | N20 | N25 | N26 | N28 | N29 | N30 | N34 | N38 | N39 | N40 | N41 | N48 | N50 | N51 | N53 | N65 | N66 | N70 | N71 | N74 | N75 | N76 | N77 | N78 | N79 | N80 | N81 | N82 | N83 | N84 | N86 | N89 | N90 | N91 | N92 | N93 | N94 | N95 | N257 | N258 | N260 | N261
		"""
		param = Conversions.enum_scalar_to_str(operating_band, enums.OperatingBandNr5G)
		self._core.io.write(f'CONFigure:NR5G:OBANd {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OperatingBandNr5G:
		"""SCPI: CONFigure[:NR5G]:OBANd \n
		Snippet: value: enums.OperatingBandNr5G = driver.applications.k14Xnr5G.configure.nr5G.oband.get() \n
		This command selects the operating band.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select at least 2 component carriers (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.NoCc.set) . \n
			:return: operating_band: N1 | N2 | N3 | N5 | N7 | N8 | N12 | N14 | N18 | N20 | N25 | N26 | N28 | N29 | N30 | N34 | N38 | N39 | N40 | N41 | N48 | N50 | N51 | N53 | N65 | N66 | N70 | N71 | N74 | N75 | N76 | N77 | N78 | N79 | N80 | N81 | N82 | N83 | N84 | N86 | N89 | N90 | N91 | N92 | N93 | N94 | N95 | N257 | N258 | N260 | N261"""
		response = self._core.io.query_str(f'CONFigure:NR5G:OBANd?')
		return Conversions.str_to_scalar_enum(response, enums.OperatingBandNr5G)
