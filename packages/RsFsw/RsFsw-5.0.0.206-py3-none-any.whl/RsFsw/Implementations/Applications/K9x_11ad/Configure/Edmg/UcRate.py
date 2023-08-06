from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UcRate:
	"""UcRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ucRate", core, parent)

	def set(self, src: enums.SourceType) -> None:
		"""SCPI: CONFigure:EDMG:UCRate \n
		Snippet: driver.applications.k9X11Ad.configure.edmg.ucRate.set(src = enums.SourceType.CUSTom) \n
		Determines whether the chip rate according to standard is used or a non-standard measurement is performed with a
		user-defined chip rate. \n
			:param src: STANdard | CUSTom STANdard Data acquisition is set to the chip rate and sample rate specified in the IEEE 802.11 ay standard. CUSTom The chip rate can be defined freely to perform a non-standard measurement.
		"""
		param = Conversions.enum_scalar_to_str(src, enums.SourceType)
		self._core.io.write(f'CONFigure:EDMG:UCRate {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceType:
		"""SCPI: CONFigure:EDMG:UCRate \n
		Snippet: value: enums.SourceType = driver.applications.k9X11Ad.configure.edmg.ucRate.get() \n
		Determines whether the chip rate according to standard is used or a non-standard measurement is performed with a
		user-defined chip rate. \n
			:return: src: STANdard | CUSTom STANdard Data acquisition is set to the chip rate and sample rate specified in the IEEE 802.11 ay standard. CUSTom The chip rate can be defined freely to perform a non-standard measurement."""
		response = self._core.io.query_str(f'CONFigure:EDMG:UCRate?')
		return Conversions.str_to_scalar_enum(response, enums.SourceType)
