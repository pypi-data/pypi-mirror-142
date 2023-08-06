from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tbw:
	"""Tbw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbw", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:IQ:TBW \n
		Snippet: driver.applications.k40PhaseNoise.sense.iq.tbw.set(bandwidth = 1.0) \n
		This command defines the maximum tracking bandwidth (sample rate) for all half decades. \n
			:param bandwidth: Range: 60 mHz to 65.28 MHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:IQ:TBW {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:IQ:TBW \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.iq.tbw.get() \n
		This command defines the maximum tracking bandwidth (sample rate) for all half decades. \n
			:return: bandwidth: Range: 60 mHz to 65.28 MHz, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:IQ:TBW?')
		return Conversions.str_to_float(response)
