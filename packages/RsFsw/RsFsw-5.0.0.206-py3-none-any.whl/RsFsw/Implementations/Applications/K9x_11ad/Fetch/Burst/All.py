from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:ALL \n
		Snippet: value: str = driver.applications.k9X11Ad.fetch.burst.all.get() \n
		This command returns all results from the default IEEE 802.11ad I/Q measurement (see 'Result Summary') . For details on
		individual parameters see 'Modulation accuracy parameters'. The results are output as a list of result strings separated
		by commas in ASCII format. The results are output in the following order: \n
			:return: result: char_data min_EVM_All,avg_EVM_All,max_EVM_All, min_EVM_Data,avg_EVM_Data,max_EVM_Data, min_EVM_Pilots,avg_EVM_Pilots,max_EVM_Pilots, min_IQ_Offset, avg_IQ_Offset,max_IQ_Offset, min_Gain_Imb,avg_Gain_Imb,max_Gain_Imb, min_Quad_Error,avg_Quad_Error,max_Quad_Error, min_CFreqErr,avg_CFreqErr,max_CFreqErr, min_SymClockErr,avg_SymClockErr,max_SymClockErr, min_RiseTime,avg_RiseTime,max_RiseTime, min_FallTime,avg_FallTime,max_FallTime, min_TimeSkew,avg_TimeSkew,max_TimeSkew, min_TDPow,avg_TDPow,max_TDPow, min_CrestFactor,avg_CrestFactor,max_CrestFactor, min_SNR,avg_SNR,max_SNR, min_HeadBER,avg_HeadBER,max_HeadBER, min_PayLBER,avg_PayLBER,max_PayLBER,"""
		response = self._core.io.query_str(f'FETCh:BURSt:ALL?')
		return trim_str_response(response)
