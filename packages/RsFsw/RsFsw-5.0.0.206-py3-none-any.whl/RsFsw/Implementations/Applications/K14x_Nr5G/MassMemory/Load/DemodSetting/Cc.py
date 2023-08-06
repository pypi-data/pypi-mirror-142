from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
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

	def set(self, filename: str, load_items: List[enums.LowerLimit] = None, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:LOAD:DEModsetting[:CC<cc>] \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.demodSetting.cc.set(filename = '1', load_items = [LowerLimit.ACLR, LowerLimit.SEM], carrierComponent = repcap.CarrierComponent.Default) \n
		This command restores the signal description. \n
			:param filename: String containing the path and name of the file. The file extension is .allocation.
			:param load_items: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('load_items', load_items, DataType.EnumList, enums.LowerLimit, True, True, 1))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write_with_opc(f'MMEMory:LOAD:DEModsetting:CC{carrierComponent_cmd_val} {param}'.rstrip())

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
