from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:MBSFn:SUBFrame<sf>:STATe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.mbsfn.subframe.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command turns MBSFN transmission in specific subframes on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:MBSFn:SUBFrame{subframe_cmd_val}:STATe {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:MBSFn:SUBFrame<sf>:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.mbsfn.subframe.state.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command turns MBSFN transmission in specific subframes on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:MBSFn:SUBFrame{subframe_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
