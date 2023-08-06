from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, meas_type: enums.MeasurementTypeK91) -> None:
		"""SCPI: CONFigure:BURSt:SPECtrum:FLATness:SELect \n
		Snippet: driver.applications.k91Wlan.configure.burst.spectrum.flatness.select.set(meas_type = enums.MeasurementTypeK91.FLATness) \n
		This remote control command configures result display type of window 2 to be either Spectrum Flatness or Group Delay.
		Results are only displayed after a measurement is executed, e.g. using the method RsFsw.Applications.K10x_Lte.Initiate.
		Immediate.set command. Note that the CONF:BURS:<ResultType>:IMM commands change the screen layout to display the
		Magnitude Capture buffer in window 1 at the top of the screen and the selected result type in window 2 below that.
		Any other active windows are closed. Use the LAYout commands to change the display (see 'Working with windows in the
		display') . \n
			:param meas_type: FLATness | GRDelay
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.MeasurementTypeK91)
		self._core.io.write(f'CONFigure:BURSt:SPECtrum:FLATness:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementTypeK91:
		"""SCPI: CONFigure:BURSt:SPECtrum:FLATness:SELect \n
		Snippet: value: enums.MeasurementTypeK91 = driver.applications.k91Wlan.configure.burst.spectrum.flatness.select.get() \n
		This remote control command configures result display type of window 2 to be either Spectrum Flatness or Group Delay.
		Results are only displayed after a measurement is executed, e.g. using the method RsFsw.Applications.K10x_Lte.Initiate.
		Immediate.set command. Note that the CONF:BURS:<ResultType>:IMM commands change the screen layout to display the
		Magnitude Capture buffer in window 1 at the top of the screen and the selected result type in window 2 below that.
		Any other active windows are closed. Use the LAYout commands to change the display (see 'Working with windows in the
		display') . \n
			:return: meas_type: FLATness | GRDelay"""
		response = self._core.io.query_str(f'CONFigure:BURSt:SPECtrum:FLATness:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementTypeK91)
