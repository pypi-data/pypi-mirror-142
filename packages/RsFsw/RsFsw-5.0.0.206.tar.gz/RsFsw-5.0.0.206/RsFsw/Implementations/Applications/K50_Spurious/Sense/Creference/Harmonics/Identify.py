from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identify:
	"""Identify commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identify", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:CREFerence:HARMonics:IDENtify \n
		Snippet: driver.applications.k50Spurious.sense.creference.harmonics.identify.set(state = False) \n
		Enables or disables the identification of harmonics of the carrier. \n
			:param state: ON | 1 HArmonics are marked OFF | 0 Harmonics are not marked
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CREFerence:HARMonics:IDENtify {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CREFerence:HARMonics:IDENtify \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.creference.harmonics.identify.get() \n
		Enables or disables the identification of harmonics of the carrier. \n
			:return: state: ON | 1 HArmonics are marked OFF | 0 Harmonics are not marked"""
		response = self._core.io.query_str(f'SENSe:CREFerence:HARMonics:IDENtify?')
		return Conversions.str_to_bool(response)
