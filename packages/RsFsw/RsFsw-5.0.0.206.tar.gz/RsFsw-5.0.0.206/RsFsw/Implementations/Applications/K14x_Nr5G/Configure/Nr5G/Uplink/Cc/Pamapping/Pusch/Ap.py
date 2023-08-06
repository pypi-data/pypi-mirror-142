from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ap:
	"""Ap commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPort, default value after init: AntennaPort.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPort_get', 'repcap_antennaPort_set', repcap.AntennaPort.Nr1)

	def repcap_antennaPort_set(self, antennaPort: repcap.AntennaPort) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPort.Default
		Default value after init: AntennaPort.Nr1"""
		self._cmd_group.set_repcap_enum_value(antennaPort)

	def repcap_antennaPort_get(self) -> repcap.AntennaPort:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default, antennaPort=repcap.AntennaPort.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PAMapping<cf>:PUSCh:AP<AntennaPort> \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pamapping.pusch.ap.set(state = False, carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default, antennaPort = repcap.AntennaPort.Default) \n
		This command selects the antenna port(s) that transmits the PUSCH. The selection indirectly also selects the antenna port
		that transmits the PUSCH DMRS. \n
			:param state: ON | OFF | 1 | 0 Turns the transmission on a specific antenna port on and off. ALL Turns on the tranmission on all antenna ports (1000 to 1011) . NONE Turns off the transmission on all antenna ports. By default, the transmission is on antenna port 1000 (configuration 1) and 1001 (configuration 2) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
			:param antennaPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ap')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		antennaPort_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPort, repcap.AntennaPort)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:PUSCh:AP{antennaPort_cmd_val} {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default, antennaPort=repcap.AntennaPort.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PAMapping<cf>:PUSCh:AP<AntennaPort> \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pamapping.pusch.ap.get(carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default, antennaPort = repcap.AntennaPort.Default) \n
		This command selects the antenna port(s) that transmits the PUSCH. The selection indirectly also selects the antenna port
		that transmits the PUSCH DMRS. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
			:param antennaPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ap')
			:return: state: ON | OFF | 1 | 0 Turns the transmission on a specific antenna port on and off. ALL Turns on the tranmission on all antenna ports (1000 to 1011) . NONE Turns off the transmission on all antenna ports. By default, the transmission is on antenna port 1000 (configuration 1) and 1001 (configuration 2) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		antennaPort_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPort, repcap.AntennaPort)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:PUSCh:AP{antennaPort_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
