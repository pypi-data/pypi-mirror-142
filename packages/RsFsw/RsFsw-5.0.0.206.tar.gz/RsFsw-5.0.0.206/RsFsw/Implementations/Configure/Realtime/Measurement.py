from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def set(self, meas_type: enums.RealtimeMeasType) -> None:
		"""SCPI: CONFigure:REALtime:MEASurement \n
		Snippet: driver.configure.realtime.measurement.set(meas_type = enums.RealtimeMeasType.HRESolution) \n
		In order to accommodate for different requirements, different measurement types are provided for Real-Time Spectrum
		measurements. These measurements are only available for R&S FSW-K161R. For R&S FSW-B512R/-B800R, the R&S FSW Real-Time
		Spectrum application always performs a 'Multi domain Real-Time Spectrum measurement'. In this case, this command is not
		available. \n
			:param meas_type: HRESolution High Resolution Real-Time measurements are performed with frequency spans of up to 160 MHz, allowing for very precise results in the frequency domain. Additional Span/RBW couplings are available for precise frequency results. Time domain evaluation is not available. MDOMain Multi Domain Real-Time measurements allow for results both in the frequency and time domains, however with spans up to 100 MHz only.
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.RealtimeMeasType)
		self._core.io.write(f'CONFigure:REALtime:MEASurement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RealtimeMeasType:
		"""SCPI: CONFigure:REALtime:MEASurement \n
		Snippet: value: enums.RealtimeMeasType = driver.configure.realtime.measurement.get() \n
		In order to accommodate for different requirements, different measurement types are provided for Real-Time Spectrum
		measurements. These measurements are only available for R&S FSW-K161R. For R&S FSW-B512R/-B800R, the R&S FSW Real-Time
		Spectrum application always performs a 'Multi domain Real-Time Spectrum measurement'. In this case, this command is not
		available. \n
			:return: meas_type: HRESolution High Resolution Real-Time measurements are performed with frequency spans of up to 160 MHz, allowing for very precise results in the frequency domain. Additional Span/RBW couplings are available for precise frequency results. Time domain evaluation is not available. MDOMain Multi Domain Real-Time measurements allow for results both in the frequency and time domains, however with spans up to 100 MHz only."""
		response = self._core.io.query_str(f'CONFigure:REALtime:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.RealtimeMeasType)
