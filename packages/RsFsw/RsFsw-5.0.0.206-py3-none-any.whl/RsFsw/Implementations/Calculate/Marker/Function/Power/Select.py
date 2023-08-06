from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, meas_type: enums.MarkerFunctionB, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:SELect \n
		Snippet: driver.calculate.marker.function.power.select.set(meas_type = enums.MarkerFunctionB.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		This command selects a power measurement and turns the measurement on. \n
			:param meas_type: ACPower | MCACpower Adjacent channel leakage ratio (ACLR) , also known as adjacent channel power or multicarrier adjacent channel. The R&S FSW performs the measurement on the trace selected with [SENSe:]POWer:TRACe. CPOWer Channel power measurement with a single carrier. The R&S FSW performs the measurement on the trace selected with [SENSe:]POWer:TRACe. OBANdwidth | OBWidth Occupied bandwidth measurement. The R&S FSW performs the measurement on the trace that marker 1 is positioned on. CN Carrier-to-noise ratio measurement. CN0 Carrier-to-noise ratio measurement referenced to 1 Hz bandwidth
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
		"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.MarkerFunctionB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:SELect {param}')
