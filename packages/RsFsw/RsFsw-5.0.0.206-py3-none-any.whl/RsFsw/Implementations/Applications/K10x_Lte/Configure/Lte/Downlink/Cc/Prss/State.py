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
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PRSS:STATe \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.prss.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns the positioning reference signal on and off. \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PRSS:STATe {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PRSS:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.downlink.cc.prss.state.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns the positioning reference signal on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PRSS:STATe?')
		return Conversions.str_to_bool(response)
