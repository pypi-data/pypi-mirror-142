from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def set(self, measurement: enums.MeasurementNr5G) -> None:
		"""SCPI: CONFigure[:NR5G]:MEASurement \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.measurement.set(measurement = enums.MeasurementNr5G.ACLR) \n
		This command selects the measurement type. \n
			:param measurement: ACLR Selects the adjacent channel leakage ratio (ACLR) measurement. CACLr Selects the Cumulative ACLR measurement. CMEasurement Selects combined EVM / ACLR / SEM measurement. ESPectrum Selects the spectrum emission mask (SEM) measurement. EVM Selects I/Q measurements. MCAClr Selects Multi-Carrier ACLR measurement. MCESpectrum Selects Multi-Carrier SEM measurement. TAERor Selects the time alignment error measurement. TPOO Selects the transmit on / off power measurement.
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MeasurementNr5G)
		self._core.io.write(f'CONFigure:NR5G:MEASurement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementNr5G:
		"""SCPI: CONFigure[:NR5G]:MEASurement \n
		Snippet: value: enums.MeasurementNr5G = driver.applications.k14Xnr5G.configure.nr5G.measurement.get() \n
		This command selects the measurement type. \n
			:return: measurement: ACLR Selects the adjacent channel leakage ratio (ACLR) measurement. CACLr Selects the Cumulative ACLR measurement. CMEasurement Selects combined EVM / ACLR / SEM measurement. ESPectrum Selects the spectrum emission mask (SEM) measurement. EVM Selects I/Q measurements. MCAClr Selects Multi-Carrier ACLR measurement. MCESpectrum Selects Multi-Carrier SEM measurement. TAERor Selects the time alignment error measurement. TPOO Selects the transmit on / off power measurement."""
		response = self._core.io.query_str(f'CONFigure:NR5G:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementNr5G)
