from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mharmonic:
	"""Mharmonic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mharmonic", core, parent)

	def set(self, harmonic: int, component=repcap.Component.Default, port=repcap.Port.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:PORT<1|2>:MHARmonic \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.port.mharmonic.set(harmonic = 1, component = repcap.Component.Default, port = repcap.Port.Default) \n
		Defines the maximum harmonic of each input frequency to be considered in calculating mixer products for spur
		identification. For details see 'Frequency plan and spur identification'. \n
			:param harmonic: Range: 1 to 5
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param port: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
		"""
		param = Conversions.decimal_value_to_str(harmonic)
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		port_cmd_val = self._cmd_group.get_repcap_cmd_value(port, repcap.Port)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:PORT{port_cmd_val}:MHARmonic {param}')

	def get(self, component=repcap.Component.Default, port=repcap.Port.Default) -> int:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:PORT<1|2>:MHARmonic \n
		Snippet: value: int = driver.applications.k50Spurious.sense.fplan.component.port.mharmonic.get(component = repcap.Component.Default, port = repcap.Port.Default) \n
		Defines the maximum harmonic of each input frequency to be considered in calculating mixer products for spur
		identification. For details see 'Frequency plan and spur identification'. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param port: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
			:return: harmonic: Range: 1 to 5"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		port_cmd_val = self._cmd_group.get_repcap_cmd_value(port, repcap.Port)
		response = self._core.io.query_str(f'SENSe:FPLan:COMPonent{component_cmd_val}:PORT{port_cmd_val}:MHARmonic?')
		return Conversions.str_to_int(response)
