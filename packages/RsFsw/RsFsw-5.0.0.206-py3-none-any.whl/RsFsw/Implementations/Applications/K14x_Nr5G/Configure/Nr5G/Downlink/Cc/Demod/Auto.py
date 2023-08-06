from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, mode: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:DEMod:AUTO \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.demod.auto.set(mode = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns automatic signal demodulation on and off. \n
			:param mode: ON | OFF | 1 | 0 ON Automatically detects the following signal properties. • Synchronization signal configuration • Bandwidth part configuration • Slot configuration • PDSCH and CORESET configuration OFF Lets you configure the signal manually.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(mode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:DEMod:AUTO {param}')
