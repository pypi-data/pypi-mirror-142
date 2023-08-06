from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: [SENSe]:SYNC[:CC<cc>][:STATe] \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.sync.cc.state.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command queries the current synchronization state. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: The string contains the following information: • OFDMSymbolTiming is the coarse symbol timing • P-SYNCSynchronization is the P-SYNC synchronization state • S-SYNCSynchronization is the S-SYNC synchronization state A zero represents a failure and a one represents a successful synchronization."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:SYNC:CC{carrierComponent_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
