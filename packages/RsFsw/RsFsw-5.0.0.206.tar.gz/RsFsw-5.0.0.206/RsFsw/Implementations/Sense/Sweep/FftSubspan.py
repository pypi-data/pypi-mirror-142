from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftSubspan:
	"""FftSubspan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fftSubspan", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:FFTSubspan \n
		Snippet: value: float = driver.sense.sweep.fftSubspan.get() \n
		Returns the number of FFT subspans required to cover the entire measurement range (read-only) . See also 'Number of
		subspans'. Only available in FFT sweep mode in the Spectrum application, and not for SEM, ACLR, or Spurious emissions
		measurements. \n
			:return: no_of_partial_spans: integer"""
		response = self._core.io.query_str(f'SENSe:SWEep:FFTSubspan?')
		return Conversions.str_to_float(response)
