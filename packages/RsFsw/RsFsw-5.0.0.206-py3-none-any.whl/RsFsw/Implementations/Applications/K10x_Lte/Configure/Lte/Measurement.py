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

	def set(self, measurement: enums.MeasurementLte) -> None:
		"""SCPI: CONFigure[:LTE]:MEASurement \n
		Snippet: driver.applications.k10Xlte.configure.lte.measurement.set(measurement = enums.MeasurementLte.ACLR) \n
		This command selects the measurement. \n
			:param measurement: ACLR Selects the Adjacent Channel Leakage Ratio measurement. CACLr Selects the Cumulative ACLR measurement. ESPectrum Selects the Spectrum Emission Mask measurement. EVM Selects I/Q measurements. MCAClr Selects Multi-Carrier ACLR measurement. MCESpectrum Selects Multi-Carrier SEM measurement. TAERor Selects the Time Alignment Error measurement. TPOO Selects the Transmit On/Off Power measurement.
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.MeasurementLte)
		self._core.io.write(f'CONFigure:LTE:MEASurement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MeasurementLte:
		"""SCPI: CONFigure[:LTE]:MEASurement \n
		Snippet: value: enums.MeasurementLte = driver.applications.k10Xlte.configure.lte.measurement.get() \n
		This command selects the measurement. \n
			:return: measurement: ACLR Selects the Adjacent Channel Leakage Ratio measurement. CACLr Selects the Cumulative ACLR measurement. ESPectrum Selects the Spectrum Emission Mask measurement. EVM Selects I/Q measurements. MCAClr Selects Multi-Carrier ACLR measurement. MCESpectrum Selects Multi-Carrier SEM measurement. TAERor Selects the Time Alignment Error measurement. TPOO Selects the Transmit On/Off Power measurement."""
		response = self._core.io.query_str(f'CONFigure:LTE:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.MeasurementLte)
