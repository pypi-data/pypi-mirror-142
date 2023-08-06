from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: FETCh[:CC<cc>]:SUMMary:EVM:DSST[:AVERage] \n
		Snippet: value: float = driver.applications.k10Xlte.fetch.cc.summary.evm.dsst.average.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the EVM of all PDSCH resource elements with a 16QAM modulation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: evm: numeric value EVM in % or dB, depending on the unit you have set."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'FETCh:CC{carrierComponent_cmd_val}:SUMMary:EVM:DSST:AVERage?')
		return Conversions.str_to_float(response)
