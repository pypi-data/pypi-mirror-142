from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sspacing:
	"""Sspacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sspacing", core, parent)

	def set(self, subcarrier_spacing: enums.SubcarrierSpacing, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:SSPacing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.sspacing.set(subcarrier_spacing = enums.SubcarrierSpacing.SS120, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the subcarrier spacing of a synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param subcarrier_spacing: SS15 15 kHz subcarrier spacing. Only for signal deployment in FR1. SS30 30 kHz subcarrier spacing. Only for signal deployment in FR1. SS120 120 kHz subcarrier spacing. Only for signal deployment in FR2. SS240 240 kHz subcarrier spacing. Only for signal deployment in FR2.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(subcarrier_spacing, enums.SubcarrierSpacing)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:SSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.SubcarrierSpacing:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:SSPacing \n
		Snippet: value: enums.SubcarrierSpacing = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.sspacing.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the subcarrier spacing of a synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: subcarrier_spacing: SS15 15 kHz subcarrier spacing. Only for signal deployment in FR1. SS30 30 kHz subcarrier spacing. Only for signal deployment in FR1. SS120 120 kHz subcarrier spacing. Only for signal deployment in FR2. SS240 240 kHz subcarrier spacing. Only for signal deployment in FR2."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:SSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.SubcarrierSpacing)
