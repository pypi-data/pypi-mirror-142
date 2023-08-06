from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nfft:
	"""Nfft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nfft", core, parent)

	def set(self, loffset: float) -> None:
		"""SCPI: [SENSe]:DIRected:NFFT \n
		Snippet: driver.applications.k50Spurious.sense.directed.nfft.set(loffset = 1.0) \n
		Defines the number of FFTs to be performed for all spurs in the directed search measurement. \n
			:param loffset: integer Range: 1 to 20, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(loffset)
		self._core.io.write(f'SENSe:DIRected:NFFT {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DIRected:NFFT \n
		Snippet: value: float = driver.applications.k50Spurious.sense.directed.nfft.get() \n
		Defines the number of FFTs to be performed for all spurs in the directed search measurement. \n
			:return: loffset: integer Range: 1 to 20, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:DIRected:NFFT?')
		return Conversions.str_to_float(response)
