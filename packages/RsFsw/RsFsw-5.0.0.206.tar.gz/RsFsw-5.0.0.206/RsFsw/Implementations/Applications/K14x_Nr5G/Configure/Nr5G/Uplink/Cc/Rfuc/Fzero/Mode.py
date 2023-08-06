from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.IqBandwidthModeNr5G, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:RFUC:FZERo:MODE \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.rfuc.fzero.mode.set(mode = enums.IqBandwidthModeNr5G.CF, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the frequency selection mode for RF upconversion.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on phase compensation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Rfuc.State.set) . \n
			:param mode: CF Converts the signal to the center frequency. MANual Converts the signal to another frequency. You can define the frequency with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Rfuc.Fzero.Frequency.set.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IqBandwidthModeNr5G)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:RFUC:FZERo:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.IqBandwidthModeNr5G:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:RFUC:FZERo:MODE \n
		Snippet: value: enums.IqBandwidthModeNr5G = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.rfuc.fzero.mode.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the frequency selection mode for RF upconversion.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on phase compensation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Rfuc.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: mode: CF Converts the signal to the center frequency. MANual Converts the signal to another frequency. You can define the frequency with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Rfuc.Fzero.Frequency.set."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:RFUC:FZERo:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IqBandwidthModeNr5G)
