from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh:FERRor[:CC<cc>][:AVERage] \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.freqError.cc.average.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the carrier frequency error. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency_error: numeric value Average, minimum or maximum frequency error, depending on the command syntax. Unit: Hz"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:FERRor:CC{carrierComponent_cmd_val}:AVERage?')
		return Conversions.str_to_float(response)
