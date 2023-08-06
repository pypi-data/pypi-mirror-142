from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PAMapping<cf>:STATe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pamapping.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default) \n
		This command selects one of the antenna port configurations.
			INTRO_CMD_HELP: Effects of this command \n
			- If you turn on a configuration, the other antenna port configuration is automatically turned off (and vice versa) . \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:STATe {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antennaPortConfig=repcap.AntennaPortConfig.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PAMapping<cf>:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pamapping.state.get(carrierComponent = repcap.CarrierComponent.Default, antennaPortConfig = repcap.AntennaPortConfig.Default) \n
		This command selects one of the antenna port configurations.
			INTRO_CMD_HELP: Effects of this command \n
			- If you turn on a configuration, the other antenna port configuration is automatically turned off (and vice versa) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antennaPortConfig: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pamapping')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antennaPortConfig_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortConfig, repcap.AntennaPortConfig)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PAMapping{antennaPortConfig_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
