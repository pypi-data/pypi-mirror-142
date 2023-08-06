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

	def set(self, test_model: str, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:LOAD:TMODel[:CC<cc>] \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.tmodel.cc.set(test_model = '1', carrierComponent = repcap.CarrierComponent.Default) \n
		This command loads an test model (NR-FR-TM) as defined by 3GPP (38.141-1 / -2) . \n
			:param test_model: String containing the name of the test model (file name) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(test_model)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:LOAD:TMODel:CC{carrierComponent_cmd_val} {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:LOAD:TMODel[:CC<cc>] \n
		Snippet: value: str = driver.applications.k14Xnr5G.massMemory.load.tmodel.cc.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command loads an test model (NR-FR-TM) as defined by 3GPP (38.141-1 / -2) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: test_model: String containing the name of the test model (file name) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:LOAD:TMODel:CC{carrierComponent_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
