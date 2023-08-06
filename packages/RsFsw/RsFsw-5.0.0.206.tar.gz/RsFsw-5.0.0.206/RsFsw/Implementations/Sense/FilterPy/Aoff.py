from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aoff:
	"""Aoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aoff", core, parent)

	def set(self, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:FILTer<n>:AOFF \n
		Snippet: driver.sense.filterPy.aoff.set(filterPy = repcap.FilterPy.Default) \n
		No command help available \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:FILTer{filterPy_cmd_val}:AOFF')

	def set_with_opc(self, filterPy=repcap.FilterPy.Default, opc_timeout_ms: int = -1) -> None:
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		"""SCPI: [SENSe]:FILTer<n>:AOFF \n
		Snippet: driver.sense.filterPy.aoff.set_with_opc(filterPy = repcap.FilterPy.Default) \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:FILTer{filterPy_cmd_val}:AOFF', opc_timeout_ms)
