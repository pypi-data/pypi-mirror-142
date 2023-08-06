from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lpy:
	"""Lpy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lpy", core, parent)

	def set(self, blocks: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:L \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.lpy.set(blocks = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of SS/PBCH blocks in the deployment range < 3 GHz.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a deployment < 3 GHz (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) .
			- Select a 30 kHz subcarrier spacing (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Sspacing.set) .
			- Select the case C block pattern (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Pattern.set) . \n
			:param blocks: 4 | 8
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(blocks)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:L {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:L \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.lpy.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of SS/PBCH blocks in the deployment range < 3 GHz.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a deployment < 3 GHz (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) .
			- Select a 30 kHz subcarrier spacing (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Sspacing.set) .
			- Select the case C block pattern (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Pattern.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: blocks: 4 | 8"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:L?')
		return Conversions.str_to_float(response)
