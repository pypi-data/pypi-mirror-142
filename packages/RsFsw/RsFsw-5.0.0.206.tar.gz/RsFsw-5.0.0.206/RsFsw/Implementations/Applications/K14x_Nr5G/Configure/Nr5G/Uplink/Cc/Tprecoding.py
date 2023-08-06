from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tprecoding:
	"""Tprecoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tprecoding", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:TPRecoding \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.tprecoding.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns transform precoding on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- When you turn on transform precoding after a preset, the R&S FSW automatically changes the relative power of the PUSCH DMRS to 3 dB, according to 3GPP 38.214. \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:TPRecoding {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:TPRecoding \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.tprecoding.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns transform precoding on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- When you turn on transform precoding after a preset, the R&S FSW automatically changes the relative power of the PUSCH DMRS to 3 dB, according to 3GPP 38.214. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:TPRecoding?')
		return Conversions.str_to_bool(response)
