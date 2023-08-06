from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rto:
	"""Rto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rto", core, parent)

	def set(self, reference: enums.SyncSignalOffsetReference, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:RTO \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.rto.set(reference = enums.SyncSignalOffsetReference.RPA, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the reference point for a synchronization signal offset.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- For selection of TxBW: Use at least one bandwidth part that has the same subcarrier spacing as the synchronization signal. For subcarrier spacing = 240 kHz, TxBW is not supported. \n
			:param reference: RPA Offset relative to the reference point A. TXBW Offset relative to the the first subcarrier.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.SyncSignalOffsetReference)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:RTO {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.SyncSignalOffsetReference:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:RTO \n
		Snippet: value: enums.SyncSignalOffsetReference = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.rto.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the reference point for a synchronization signal offset.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- For selection of TxBW: Use at least one bandwidth part that has the same subcarrier spacing as the synchronization signal. For subcarrier spacing = 240 kHz, TxBW is not supported. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: reference: RPA Offset relative to the reference point A. TXBW Offset relative to the the first subcarrier."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:RTO?')
		return Conversions.str_to_scalar_enum(response, enums.SyncSignalOffsetReference)
