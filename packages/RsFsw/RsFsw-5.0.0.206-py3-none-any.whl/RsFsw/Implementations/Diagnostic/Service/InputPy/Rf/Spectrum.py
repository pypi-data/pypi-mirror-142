from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	def set(self, bandwidth: enums.ServiceBandwidth) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:RF[:SPECtrum] \n
		Snippet: driver.diagnostic.service.inputPy.rf.spectrum.set(bandwidth = enums.ServiceBandwidth.BROadband) \n
		This command selects the bandwidth of the calibration signal. \n
			:param bandwidth: NARRowband | BROadband NARRowband Narrowband signal for power calibration of the frontend. BROadband Broadband signal for calibration of the IF filter.
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.ServiceBandwidth)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:RF:SPECtrum {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ServiceBandwidth:
		"""SCPI: DIAGnostic:SERVice:INPut:RF[:SPECtrum] \n
		Snippet: value: enums.ServiceBandwidth = driver.diagnostic.service.inputPy.rf.spectrum.get() \n
		This command selects the bandwidth of the calibration signal. \n
			:return: bandwidth: NARRowband | BROadband NARRowband Narrowband signal for power calibration of the frontend. BROadband Broadband signal for calibration of the IF filter."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:RF:SPECtrum?')
		return Conversions.str_to_scalar_enum(response, enums.ServiceBandwidth)
