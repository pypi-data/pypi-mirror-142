from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ap:
	"""Ap commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPort3k, default value after init: AntennaPort3k.Nr3000"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPort3k_get', 'repcap_antennaPort3k_set', repcap.AntennaPort3k.Nr3000)

	def repcap_antennaPort3k_set(self, antennaPort3k: repcap.AntennaPort3k) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPort3k.Default
		Default value after init: AntennaPort3k.Nr3000"""
		self._cmd_group.set_repcap_enum_value(antennaPort3k)

	def repcap_antennaPort3k_get(self) -> repcap.AntennaPort3k:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default, antennaPort3k=repcap.AntennaPort3k.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:PAMapping<cf>:CSIRs:AP<AntennaPort3k> \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.pamapping.csirs.ap.set(state = False, carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default, antennaPort3k = repcap.AntennaPort3k.Default) \n
		This command selects the antenna port(s) on which the CSI reference signal is transmitted. \n
			:param state: ON | OFF | 1 | 0 Turns a specific CSI-RS antenna port on and off. ALL | NONE Turns all CSI-RS antenna port on and off.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
			:param antennaPort3k: optional repeated capability selector. Default value: Nr3000 (settable in the interface 'Ap')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		antennaPort3k_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPort3k, repcap.AntennaPort3k)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:CSIRs:AP{antennaPort3k_cmd_val} {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default, antennaPort3k=repcap.AntennaPort3k.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:PAMapping<cf>:CSIRs:AP<AntennaPort3k> \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.pamapping.csirs.ap.get(carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default, antennaPort3k = repcap.AntennaPort3k.Default) \n
		This command selects the antenna port(s) on which the CSI reference signal is transmitted. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
			:param antennaPort3k: optional repeated capability selector. Default value: Nr3000 (settable in the interface 'Ap')
			:return: state: ON | OFF | 1 | 0 Turns a specific CSI-RS antenna port on and off. ALL | NONE Turns all CSI-RS antenna port on and off."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		antennaPort3k_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPort3k, repcap.AntennaPort3k)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:CSIRs:AP{antennaPort3k_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
