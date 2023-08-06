from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:STORe:MDPD:WAVeform \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.mdpd.waveform.set(filename = '1') \n
		Saves the memory polynomial waveform at a user selected path. Only available when generator control is OFF. \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:STORe:MDPD:WAVeform {param}')
