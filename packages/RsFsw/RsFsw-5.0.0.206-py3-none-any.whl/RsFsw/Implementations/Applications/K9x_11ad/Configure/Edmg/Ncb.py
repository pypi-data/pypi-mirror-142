from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncb:
	"""Ncb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncb", core, parent)

	def set(self, ncb: int) -> None:
		"""SCPI: CONFigure:EDMG:NCB \n
		Snippet: driver.applications.k9X11Ad.configure.edmg.ncb.set(ncb = 1) \n
		Indicates the number of contiguous 2.16 GHz channels the measurement was made for. Note that the R&S FSW hardware
		currently only supports measurement bandwidths up to a maximum of 5 GHz (using bandwidth extension options) .
		Thus, measurements with 3 or 4 channels can only be performed on data from input files or using downsampling (see method
		RsFsw.Applications.K9x_11ad.Configure.Edmg.Crate.set) . \n
			:param ncb: 1 | 2 | 3 | 4
		"""
		param = Conversions.decimal_value_to_str(ncb)
		self._core.io.write(f'CONFigure:EDMG:NCB {param}')

	def get(self) -> int:
		"""SCPI: CONFigure:EDMG:NCB \n
		Snippet: value: int = driver.applications.k9X11Ad.configure.edmg.ncb.get() \n
		Indicates the number of contiguous 2.16 GHz channels the measurement was made for. Note that the R&S FSW hardware
		currently only supports measurement bandwidths up to a maximum of 5 GHz (using bandwidth extension options) .
		Thus, measurements with 3 or 4 channels can only be performed on data from input files or using downsampling (see method
		RsFsw.Applications.K9x_11ad.Configure.Edmg.Crate.set) . \n
			:return: ncb: 1 | 2 | 3 | 4"""
		response = self._core.io.query_str(f'CONFigure:EDMG:NCB?')
		return Conversions.str_to_int(response)
