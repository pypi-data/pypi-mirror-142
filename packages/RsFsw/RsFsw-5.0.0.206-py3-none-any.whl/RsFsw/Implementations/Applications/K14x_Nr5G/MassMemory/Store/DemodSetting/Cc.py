from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, carrierComponent: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponent)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, filename: str, store=repcap.Store.Default, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:DEModsetting[:CC<cc>] \n
		Snippet: driver.applications.k14Xnr5G.massMemory.store.demodSetting.cc.set(filename = '1', store = repcap.Store.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		This command saves the signal description. \n
			:param filename: String containing the path and name of the file. The file extension is .allocation.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:DEModsetting:CC{carrierComponent_cmd_val} {param}')

	def get(self, store=repcap.Store.Default, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:DEModsetting[:CC<cc>] \n
		Snippet: value: str = driver.applications.k14Xnr5G.massMemory.store.demodSetting.cc.get(store = repcap.Store.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		This command saves the signal description. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: filename: String containing the path and name of the file. The file extension is .allocation."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:DEModsetting:CC{carrierComponent_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
