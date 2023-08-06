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

	def set(self, spectrum: enums.ServiceBandwidth) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:EMI[:SPECtrum] \n
		Snippet: driver.diagnostic.service.inputPy.emi.spectrum.set(spectrum = enums.ServiceBandwidth.BROadband) \n
		No command help available \n
			:param spectrum: No help available
		"""
		param = Conversions.enum_scalar_to_str(spectrum, enums.ServiceBandwidth)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:EMI:SPECtrum {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ServiceBandwidth:
		"""SCPI: DIAGnostic:SERVice:INPut:EMI[:SPECtrum] \n
		Snippet: value: enums.ServiceBandwidth = driver.diagnostic.service.inputPy.emi.spectrum.get() \n
		No command help available \n
			:return: spectrum: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:EMI:SPECtrum?')
		return Conversions.str_to_scalar_enum(response, enums.ServiceBandwidth)
