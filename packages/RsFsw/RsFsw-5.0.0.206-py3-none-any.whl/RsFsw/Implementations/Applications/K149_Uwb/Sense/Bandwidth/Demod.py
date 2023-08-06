from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth:DEMod \n
		Snippet: value: float = driver.applications.k149Uwb.sense.bandwidth.demod.get() \n
		No command help available \n
			:return: bandwidth: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:DEMod?')
		return Conversions.str_to_float(response)
