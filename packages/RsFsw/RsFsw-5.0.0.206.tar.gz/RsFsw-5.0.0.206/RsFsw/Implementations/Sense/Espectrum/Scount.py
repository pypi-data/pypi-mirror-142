from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scount", core, parent)

	def set(self, subblocks: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:SCOunt \n
		Snippet: driver.sense.espectrum.scount.set(subblocks = 1.0, subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. \n
			:param subblocks: Number of sub blocks in the SEM measurement. Range: 1 to 8
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(subblocks)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:SCOunt {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:SCOunt \n
		Snippet: value: float = driver.sense.espectrum.scount.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: subblocks: Number of sub blocks in the SEM measurement. Range: 1 to 8"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:SCOunt?')
		return Conversions.str_to_float(response)
