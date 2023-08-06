from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scft:
	"""Scft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scft", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:RPA:KZERo:SCFT \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.rpa.kzero.scft.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an offset relative to reference point A for bandwidth parts with 15 kHz subcarrier spacing.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Bandwidth part with 15 kHz subcarrier spacing is available. \n
			:param offset: -6 | 0 | 6
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:RPA:KZERo:SCFT {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:RPA:KZERo:SCFT \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.rpa.kzero.scft.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines an offset relative to reference point A for bandwidth parts with 15 kHz subcarrier spacing.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Bandwidth part with 15 kHz subcarrier spacing is available. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: -6 | 0 | 6"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:RPA:KZERo:SCFT?')
		return Conversions.str_to_float(response)
