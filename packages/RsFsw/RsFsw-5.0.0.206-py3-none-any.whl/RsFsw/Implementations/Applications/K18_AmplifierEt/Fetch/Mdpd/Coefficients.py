from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficients:
	"""Coefficients commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficients", core, parent)

	def get(self) -> List[float]:
		"""SCPI: FETCh:MDPD:COEFficients \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.fetch.mdpd.coefficients.get() \n
		Fetches the MDPD coefficient values. \n
			:return: coefficient: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:MDPD:COEFficients?')
		return response
