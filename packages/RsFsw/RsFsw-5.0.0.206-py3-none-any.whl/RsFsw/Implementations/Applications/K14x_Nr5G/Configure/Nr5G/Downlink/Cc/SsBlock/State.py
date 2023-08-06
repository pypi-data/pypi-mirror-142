from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, ssBlock=repcap.SsBlock.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock[:STATe<ss>] \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default, ssBlock = repcap.SsBlock.Default) \n
		This command turns an individual SS/PBCH block on and off. \n
			:param state: ALL Turns on all synchronization blocks. NONE Turns off all synchronization blocks. ON | 1 Turns on a single synchronization block (selected by the suffix at STATe) . ON | 1 Turns off a single synchronization block (selected by the suffix at STATe) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param ssBlock: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SsBlock')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		ssBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(ssBlock, repcap.SsBlock)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:STATe{ssBlock_cmd_val} {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, ssBlock=repcap.SsBlock.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock[:STATe<ss>] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.state.get(carrierComponent = repcap.CarrierComponent.Default, ssBlock = repcap.SsBlock.Default) \n
		This command turns an individual SS/PBCH block on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param ssBlock: optional repeated capability selector. Default value: Nr0 (settable in the interface 'SsBlock')
			:return: state: ALL Turns on all synchronization blocks. NONE Turns off all synchronization blocks. ON | 1 Turns on a single synchronization block (selected by the suffix at STATe) . ON | 1 Turns off a single synchronization block (selected by the suffix at STATe) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		ssBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(ssBlock, repcap.SsBlock)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:STATe{ssBlock_cmd_val}?')
		return Conversions.str_to_bool(response)
