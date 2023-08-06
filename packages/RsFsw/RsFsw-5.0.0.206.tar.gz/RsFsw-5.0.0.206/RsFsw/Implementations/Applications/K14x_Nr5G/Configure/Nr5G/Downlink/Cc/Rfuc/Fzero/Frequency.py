from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:RFUC:FZERo:FREQuency \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.rfuc.fzero.frequency.set(frequency = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects a frequency for RF upconversion.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on phase compensation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Rfuc.State.set) .
			- Select mode to select custom frequency (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Rfuc.Fzero.Mode.set) . \n
			:param frequency: numeric value Unit: Hz
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:RFUC:FZERo:FREQuency {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:RFUC:FZERo:FREQuency \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.rfuc.fzero.frequency.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects a frequency for RF upconversion.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on phase compensation (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Rfuc.State.set) .
			- Select mode to select custom frequency (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Rfuc.Fzero.Mode.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency: numeric value Unit: Hz"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:RFUC:FZERo:FREQuency?')
		return Conversions.str_to_float(response)
