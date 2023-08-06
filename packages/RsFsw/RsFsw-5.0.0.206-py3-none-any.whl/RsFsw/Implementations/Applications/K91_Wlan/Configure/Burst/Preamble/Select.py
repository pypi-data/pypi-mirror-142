from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, err_type: enums.ErrorType) -> None:
		"""SCPI: CONFigure:BURSt:PREamble:SELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.preamble.select.set(err_type = enums.ErrorType.FREQuency) \n
		This remote control command specifies whether frequency or phase results are displayed when the measurement type is set
		to Error Vs Preamble (method RsFsw.Applications.K91_Wlan.Configure.Burst.Preamble.Immediate.set) . \n
			:param err_type: FREQuency | PHASe FREQuency Displays frequency error results for the preamble of the measured PPDUs only PHASe Displays phase error results for the preamble of the measured PPDUs only
		"""
		param = Conversions.enum_scalar_to_str(err_type, enums.ErrorType)
		self._core.io.write(f'CONFigure:BURSt:PREamble:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ErrorType:
		"""SCPI: CONFigure:BURSt:PREamble:SELect \n
		Snippet: value: enums.ErrorType = driver.applications.k91Wlan.configure.burst.preamble.select.get() \n
		This remote control command specifies whether frequency or phase results are displayed when the measurement type is set
		to Error Vs Preamble (method RsFsw.Applications.K91_Wlan.Configure.Burst.Preamble.Immediate.set) . \n
			:return: err_type: FREQuency | PHASe FREQuency Displays frequency error results for the preamble of the measured PPDUs only PHASe Displays phase error results for the preamble of the measured PPDUs only"""
		response = self._core.io.query_str(f'CONFigure:BURSt:PREamble:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.ErrorType)
