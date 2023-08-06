from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, component=repcap.Component.Default, port=repcap.Port.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:PORT<1|2>:FREQuency \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.port.frequency.set(frequency = 1.0, component = repcap.Component.Default, port = repcap.Port.Default) \n
		Defines the frequency of the input signal. For all components after the first one, the output frequency of the previous
		component is used as the input frequency. For details see 'Frequency plan and spur identification'. \n
			:param frequency: Unit: HZ
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param port: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		port_cmd_val = self._cmd_group.get_repcap_cmd_value(port, repcap.Port)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:PORT{port_cmd_val}:FREQuency {param}')

	def get(self, component=repcap.Component.Default, port=repcap.Port.Default) -> float:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:PORT<1|2>:FREQuency \n
		Snippet: value: float = driver.applications.k50Spurious.sense.fplan.component.port.frequency.get(component = repcap.Component.Default, port = repcap.Port.Default) \n
		Defines the frequency of the input signal. For all components after the first one, the output frequency of the previous
		component is used as the input frequency. For details see 'Frequency plan and spur identification'. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param port: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
			:return: frequency: Unit: HZ"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		port_cmd_val = self._cmd_group.get_repcap_cmd_value(port, repcap.Port)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:PORT{port_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
