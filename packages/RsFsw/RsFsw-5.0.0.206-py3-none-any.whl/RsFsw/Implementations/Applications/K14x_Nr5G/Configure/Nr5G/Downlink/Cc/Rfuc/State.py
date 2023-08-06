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

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:RFUC:STATe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.rfuc.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns RF upconversion and corresponding phase compensation on and off. \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:RFUC:STATe {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:RFUC:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.rfuc.state.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns RF upconversion and corresponding phase compensation on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:RFUC:STATe?')
		return Conversions.str_to_bool(response)
