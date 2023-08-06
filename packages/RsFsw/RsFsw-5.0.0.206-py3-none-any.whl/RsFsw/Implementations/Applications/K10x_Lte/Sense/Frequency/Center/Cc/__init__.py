from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 2 total commands, 1 Subgroups, 1 group commands
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

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	def set(self, frequency: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer[:CC<cc>] \n
		Snippet: driver.applications.k10Xlte.sense.frequency.center.cc.set(frequency = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the center frequency for RF measurements.
			INTRO_CMD_HELP: Component carrier measurements \n
			- Defining or querying the frequency of the first carrier is possible with FREQ:CENT:CC1. The CC1 part of the syntax is mandatory in that case.
			- FREQ:CENT? queries the measurement frequency (center of the two carriers) . \n
			:param frequency: numeric value Range: fmin to fmax , Unit: Hz
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:FREQuency:CENTer:CC{carrierComponent_cmd_val} {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer[:CC<cc>] \n
		Snippet: value: float = driver.applications.k10Xlte.sense.frequency.center.cc.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the center frequency for RF measurements.
			INTRO_CMD_HELP: Component carrier measurements \n
			- Defining or querying the frequency of the first carrier is possible with FREQ:CENT:CC1. The CC1 part of the syntax is mandatory in that case.
			- FREQ:CENT? queries the measurement frequency (center of the two carriers) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency: numeric value Range: fmin to fmax , Unit: Hz"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:CC{carrierComponent_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
