from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: MimoAntenna, default value after init: MimoAntenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_mimoAntenna_get', 'repcap_mimoAntenna_set', repcap.MimoAntenna.Nr1)

	def repcap_mimoAntenna_set(self, mimoAntenna: repcap.MimoAntenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to MimoAntenna.Default
		Default value after init: MimoAntenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(mimoAntenna)

	def repcap_mimoAntenna_get(self) -> repcap.MimoAntenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, port: enums.Port, mimoAntenna=repcap.MimoAntenna.Default) -> None:
		"""SCPI: TRIGger[:SEQuence]:PORT<ant> \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.port.set(port = enums.Port.PORT1, mimoAntenna = repcap.MimoAntenna.Default) \n
		This command selects the trigger port for measurements with devices that have several trigger ports. \n
			:param port: PORT1 PORT2 PORT3
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
		"""
		param = Conversions.enum_scalar_to_str(port, enums.Port)
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		self._core.io.write(f'TRIGger:SEQuence:PORT{mimoAntenna_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, mimoAntenna=repcap.MimoAntenna.Default) -> enums.Port:
		"""SCPI: TRIGger[:SEQuence]:PORT<ant> \n
		Snippet: value: enums.Port = driver.applications.k10Xlte.trigger.sequence.port.get(mimoAntenna = repcap.MimoAntenna.Default) \n
		This command selects the trigger port for measurements with devices that have several trigger ports. \n
			:param mimoAntenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Port')
			:return: port: PORT1 PORT2 PORT3"""
		mimoAntenna_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoAntenna, repcap.MimoAntenna)
		response = self._core.io.query_str(f'TRIGger:SEQuence:PORT{mimoAntenna_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.Port)

	def clone(self) -> 'Port':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Port(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
