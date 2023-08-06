from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tframe:
	"""Tframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tframe", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh[:CC<cc>]:SUMMary:TFRame \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.cc.summary.tframe.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the (sub) frame start offset as shown in the capture buffer. Note that you have to select a
		particular subframe; otherwise the command returns an error. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: Time difference between the (sub) frame start and capture buffer start. Unit: s"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:CC{carrierComponent_cmd_val}:SUMMary:TFRame?')
		return Conversions.str_to_float(response)
