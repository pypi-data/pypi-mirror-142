from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mnumber:
	"""Mnumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mnumber", core, parent)

	def set(self, mharm: float) -> None:
		"""SCPI: [SENSe]:CREFerence:HARMonics:MNUMber \n
		Snippet: driver.applications.k50Spurious.sense.creference.harmonics.mnumber.set(mharm = 1.0) \n
		Sets the maximum harmonics number to be measured. \n
			:param mharm: numeric value
		"""
		param = Conversions.decimal_value_to_str(mharm)
		self._core.io.write(f'SENSe:CREFerence:HARMonics:MNUMber {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CREFerence:HARMonics:MNUMber \n
		Snippet: value: float = driver.applications.k50Spurious.sense.creference.harmonics.mnumber.get() \n
		Sets the maximum harmonics number to be measured. \n
			:return: mharm: No help available"""
		response = self._core.io.query_str(f'SENSe:CREFerence:HARMonics:MNUMber?')
		return Conversions.str_to_float(response)
