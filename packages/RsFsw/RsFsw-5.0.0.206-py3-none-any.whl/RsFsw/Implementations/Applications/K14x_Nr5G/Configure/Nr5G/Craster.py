from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Craster:
	"""Craster commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("craster", core, parent)

	def set(self, bandwidth: enums.BandwidthChRaster) -> None:
		"""SCPI: CONFigure[:NR5G]:CRASter \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.craster.set(bandwidth = enums.BandwidthChRaster.C100) \n
		This command selects the channel raster of a component carrier.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select an operating band that supports different channel raster (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oband.set) . For all other operating bands, the command works as a query only. \n
			:param bandwidth: C15 15 kHz channel rater C15 100 kHz channel rater
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.BandwidthChRaster)
		self._core.io.write(f'CONFigure:NR5G:CRASter {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BandwidthChRaster:
		"""SCPI: CONFigure[:NR5G]:CRASter \n
		Snippet: value: enums.BandwidthChRaster = driver.applications.k14Xnr5G.configure.nr5G.craster.get() \n
		This command selects the channel raster of a component carrier.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select an operating band that supports different channel raster (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Oband.set) . For all other operating bands, the command works as a query only. \n
			:return: bandwidth: C15 15 kHz channel rater C15 100 kHz channel rater"""
		response = self._core.io.query_str(f'CONFigure:NR5G:CRASter?')
		return Conversions.str_to_scalar_enum(response, enums.BandwidthChRaster)
