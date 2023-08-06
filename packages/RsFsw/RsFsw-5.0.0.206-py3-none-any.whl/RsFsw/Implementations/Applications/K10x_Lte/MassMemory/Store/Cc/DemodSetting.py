from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodSetting:
	"""DemodSetting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodSetting", core, parent)

	def set(self, arg_0: str, store=repcap.Store.Default, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:STORe<n>[:CC<cc>]:DEModsetting \n
		Snippet: driver.applications.k10Xlte.massMemory.store.cc.demodSetting.set(arg_0 = '1', store = repcap.Store.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		This command saves the signal description. \n
			:param arg_0: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:CC{carrierComponent_cmd_val}:DEModsetting {param}')

	def get(self, store=repcap.Store.Default, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:STORe<n>[:CC<cc>]:DEModsetting \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.store.cc.demodSetting.get(store = repcap.Store.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		This command saves the signal description. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: arg_0: No help available"""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:CC{carrierComponent_cmd_val}:DEModsetting?')
		return trim_str_response(response)
