from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: SPortPair, default value after init: SPortPair.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_sPortPair_get', 'repcap_sPortPair_set', repcap.SPortPair.Ix1)

	def repcap_sPortPair_set(self, sPortPair: repcap.SPortPair) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SPortPair.Default
		Default value after init: SPortPair.Ix1"""
		self._cmd_group.set_repcap_enum_value(sPortPair)

	def repcap_sPortPair_get(self) -> repcap.SPortPair:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, touchStone=repcap.TouchStone.Default, sPortPair=repcap.SPortPair.Default) -> float:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SLISt<sli>:DATA:PHASe<spi> \n
		Snippet: value: float = driver.sense.correction.fresponse.user.slist.data.phase.get(touchStone = repcap.TouchStone.Default, sPortPair = repcap.SPortPair.Default) \n
		Queries the trace values for the specified .snp file and ports. \n
			:param touchStone: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Slist')
			:param sPortPair: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Phase')
			:return: result: No help available"""
		touchStone_cmd_val = self._cmd_group.get_repcap_cmd_value(touchStone, repcap.TouchStone)
		sPortPair_cmd_val = self._cmd_group.get_repcap_cmd_value(sPortPair, repcap.SPortPair)
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:SLISt{touchStone_cmd_val}:DATA:PHASe{sPortPair_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Phase':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Phase(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
