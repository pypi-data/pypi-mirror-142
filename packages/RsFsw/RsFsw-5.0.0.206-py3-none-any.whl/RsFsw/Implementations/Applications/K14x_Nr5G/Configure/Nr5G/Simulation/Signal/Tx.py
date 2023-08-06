from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antenna_get', 'repcap_antenna_set', repcap.Antenna.Nr1)

	def repcap_antenna_set(self, antenna: repcap.Antenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Antenna.Default
		Default value after init: Antenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(antenna)

	def repcap_antenna_get(self) -> repcap.Antenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, arg_0: str, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:SIMulation:SIGNal:TX<ant> \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.simulation.signal.tx.set(arg_0 = '1', antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:NR5G:SIMulation:SIGNal:TX{antenna_cmd_val} {param}')

	def get(self, antenna=repcap.Antenna.Default) -> str:
		"""SCPI: CONFigure[:NR5G]:SIMulation:SIGNal:TX<ant> \n
		Snippet: value: str = driver.applications.k14Xnr5G.configure.nr5G.simulation.signal.tx.get(antenna = repcap.Antenna.Default) \n
		No command help available \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tx')
			:return: arg_0: No help available"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:NR5G:SIMulation:SIGNal:TX{antenna_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
