from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get(self) -> List[float]:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SPECtrum:DATA:FREQuency \n
		Snippet: value: List[float] = driver.sense.correction.fresponse.user.spectrum.data.frequency.get() \n
		Queries the trace values for the combined user correction files (.snp+.fres) in Spectrum mode. \n
			:return: trace_data: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;SENSe:CORRection:FRESponse:USER:SPECtrum:DATA:FREQuency?')
		return response
