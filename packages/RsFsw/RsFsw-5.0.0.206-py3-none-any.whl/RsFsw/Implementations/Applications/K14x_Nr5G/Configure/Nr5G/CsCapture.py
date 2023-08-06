from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsCapture:
	"""CsCapture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csCapture", core, parent)

	def set(self, mode: enums.SweepMode) -> None:
		"""SCPI: CONFigure[:NR5G]:CSCapture \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.csCapture.set(mode = enums.SweepMode.AUTO) \n
		This command selects the capture mode for measurements on multiple component carriers. \n
			:param mode: AUTO Automatically selects the number of component carriers that can be analyzed in a single capture. If there are more carriers than can be analyzed in a single measurement, the other carriers are analyzed in subsequent measurements. SINGle Capture each component carrier subsequently in individual measurements.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SweepMode)
		self._core.io.write(f'CONFigure:NR5G:CSCapture {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepMode:
		"""SCPI: CONFigure[:NR5G]:CSCapture \n
		Snippet: value: enums.SweepMode = driver.applications.k14Xnr5G.configure.nr5G.csCapture.get() \n
		This command selects the capture mode for measurements on multiple component carriers. \n
			:return: mode: AUTO Automatically selects the number of component carriers that can be analyzed in a single capture. If there are more carriers than can be analyzed in a single measurement, the other carriers are analyzed in subsequent measurements. SINGle Capture each component carrier subsequently in individual measurements."""
		response = self._core.io.query_str(f'CONFigure:NR5G:CSCapture?')
		return Conversions.str_to_scalar_enum(response, enums.SweepMode)
