from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal.Utilities import trim_str_response
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>[:CC<cc>][:ISRC][:FRAMe<fr>]:SUMMary:EVM:SDSF:MAXimum:RESult \n
		Snippet: value: str = driver.applications.k14Xnr5G.calculate.limit.cc.isrc.frame.summary.evm.sdsf.maximum.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		This command queries the limit specified by 3GPP for the EVM of all PUSCH DMRS resource elements with a 64QAM modulation. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:return: limit_check: FAILED Limit check has failed. PASSED Limit check has passed. NOTEVALUATED Limits have not been evaluated."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CC{carrierComponent_cmd_val}:ISRC:FRAMe{frame_cmd_val}:SUMMary:EVM:SDSF:MAXimum:RESult?')
		return trim_str_response(response)
