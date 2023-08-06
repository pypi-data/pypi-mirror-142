from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer[:RRC][:STATe] \n
		Snippet: driver.sense.espectrum.filterPy.rrc.state.set(state = False, subBlock = repcap.SubBlock.Default) \n
		This command turns the RRC filter in the reference range on and off. The RRC filter is available if the power reference
		is the channel power. \n
			:param state: ON | OFF | 0 | 1
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer:RRC:STATe {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer[:RRC][:STATe] \n
		Snippet: value: bool = driver.sense.espectrum.filterPy.rrc.state.get(subBlock = repcap.SubBlock.Default) \n
		This command turns the RRC filter in the reference range on and off. The RRC filter is available if the power reference
		is the channel power. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: state: ON | OFF | 0 | 1"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer:RRC:STATe?')
		return Conversions.str_to_bool(response)
