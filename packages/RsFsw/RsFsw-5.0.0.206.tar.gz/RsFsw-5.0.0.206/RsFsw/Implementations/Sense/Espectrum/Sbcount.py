from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sbcount:
	"""Sbcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sbcount", core, parent)

	def set(self, subblocks: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:SBCount \n
		Snippet: driver.sense.espectrum.sbcount.set(subblocks = 1.0, subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. Note that this command is maintained for
		compatibility reasons only. For newer remote control programs use the [SENSe:]ESPectrum<sb>:SCOunt command. \n
			:param subblocks: Number of sub blocks in the SEM measurement. Range: 1 to 3
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(subblocks)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:SBCount {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:SBCount \n
		Snippet: value: float = driver.sense.espectrum.sbcount.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the number of sub blocks in the SEM measurement. Note that this command is maintained for
		compatibility reasons only. For newer remote control programs use the [SENSe:]ESPectrum<sb>:SCOunt command. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: subblocks: Number of sub blocks in the SEM measurement. Range: 1 to 3"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:SBCount?')
		return Conversions.str_to_float(response)
