from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hspeed:
	"""Hspeed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hspeed", core, parent)

	def set(self, state: bool, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:HSPeed \n
		Snippet: driver.sense.espectrum.hspeed.set(state = False, subBlock = repcap.SubBlock.Default) \n
		This command turns high speed mode for SEM measurements on and off. For more information including restrictions see 'Fast
		SEM measurements'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:HSPeed {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:HSPeed \n
		Snippet: value: bool = driver.sense.espectrum.hspeed.get(subBlock = repcap.SubBlock.Default) \n
		This command turns high speed mode for SEM measurements on and off. For more information including restrictions see 'Fast
		SEM measurements'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:HSPeed?')
		return Conversions.str_to_bool(response)
