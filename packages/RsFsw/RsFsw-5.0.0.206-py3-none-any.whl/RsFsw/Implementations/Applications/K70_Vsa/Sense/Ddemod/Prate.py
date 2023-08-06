from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prate:
	"""Prate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prate", core, parent)

	def set(self, capt_oversampling: float) -> None:
		"""SCPI: [SENSe]:DDEMod:PRATe \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.prate.set(capt_oversampling = 1.0) \n
		Defines the number of samples that are captured per symbol, i.e. the factor by which the symbol rate is multiplied to
		obtain the sample rate. This parameter also affects the demodulation bandwidth and thus the usable I/Q bandwidth.
		The sample rate depends on the defined 'Symbol Rate' (see 'Sample rate, symbol rate and I/Q bandwidth') . \n
			:param capt_oversampling: | 2 | 4 | 8 | 16 | 32 | 64 | 128 The factor by which the symbol rate is multiplied to obtain the sample rate, e.g. 4 samples per symbol: sample rate = 4*symbol rate
		"""
		param = Conversions.decimal_value_to_str(capt_oversampling)
		self._core.io.write(f'SENSe:DDEMod:PRATe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:PRATe \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.prate.get() \n
		Defines the number of samples that are captured per symbol, i.e. the factor by which the symbol rate is multiplied to
		obtain the sample rate. This parameter also affects the demodulation bandwidth and thus the usable I/Q bandwidth.
		The sample rate depends on the defined 'Symbol Rate' (see 'Sample rate, symbol rate and I/Q bandwidth') . \n
			:return: capt_oversampling: | 2 | 4 | 8 | 16 | 32 | 64 | 128 The factor by which the symbol rate is multiplied to obtain the sample rate, e.g. 4 samples per symbol: sample rate = 4*symbol rate"""
		response = self._core.io.query_str(f'SENSe:DDEMod:PRATe?')
		return Conversions.str_to_float(response)
