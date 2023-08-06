from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spur:
	"""Spur commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spur", core, parent)

	def set(self, spur: List[int] = None) -> None:
		"""SCPI: [SENSe]:TRANsfer:SPUR \n
		Snippet: driver.applications.k50Spurious.sense.transfer.spur.set(spur = [1, 2, 3]) \n
		No command help available \n
			:param spur: Comma-separated list of spur numbers (integers)
		"""
		param = ''
		if spur:
			param = Conversions.list_to_csv_str(spur)
		self._core.io.write(f'SENSe:TRANsfer:SPUR {param}'.strip())
