from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self, measurement: enums.MeasurementLteResult = None, window=repcap.Window.Default, marker=repcap.Marker.Default, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer<sb>:RESult[:CURRent] \n
		Snippet: value: float = driver.applications.k10Xlte.calculate.marker.function.power.result.current.get(measurement = enums.MeasurementLteResult.ACPower, window = repcap.Window.Default, marker = repcap.Marker.Default, subBlock = repcap.SubBlock.Default) \n
		This command queries the results of the ACLR measurement or the total signal power level of the SEM measurement. To get a
		valid result, you have to perform a complete measurement with synchronization to the end of the measurement before
		reading out the result. This is only possible for single sweeps. \n
			:param measurement: CPOW This parameter queries the channel power of the reference range. MCAC Queries the channel powers of the ACLR, MC ACLR and Cumulative ACLR measurements as shown in the ACLR table. Where available, this parameter also queries the power of the adjacent channels (for example in the ACLR measurement) . GACLr Queries the ACLR values for each gap channel in the MC ACLR measurement.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Power')
			:return: result: Results for the Spectrum Emission Mask measurement: Power level in dBm. Results for the ACLR measurements: Relative power levels of the ACLR channels. The number of return values depends on the number of transmission and adjacent channels. The order of return values is: • TXChannelPower is the power of the transmission channel in dBm • LowerAdjChannelPower is the relative power of the lower adjacent channel in dB • UpperAdjChannelPower is the relative power of the upper adjacent channel in dB • 1stLowerAltChannelPower is the relative power of the first lower alternate channel in dB • 1stUpperAltChannelPower is the relative power of the first lower alternate channel in dB (...) • nthLowerAltChannelPower is the relative power of a subsequent lower alternate channel in dB • nthUpperAltChannelPower is the relative power of a subsequent lower alternate channel in dB"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('measurement', measurement, DataType.Enum, enums.MeasurementLteResult, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer{subBlock_cmd_val}:RESult:CURRent? {param}'.rstrip())
		return Conversions.str_to_float(response)
