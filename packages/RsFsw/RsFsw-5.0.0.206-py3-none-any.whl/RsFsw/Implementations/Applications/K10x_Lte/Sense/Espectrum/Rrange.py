from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rrange:
	"""Rrange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrange", core, parent)

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RRANge \n
		Snippet: value: float = driver.applications.k10Xlte.sense.espectrum.rrange.get(subBlock = repcap.SubBlock.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: range_py: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RRANge?')
		return Conversions.str_to_float(response)
