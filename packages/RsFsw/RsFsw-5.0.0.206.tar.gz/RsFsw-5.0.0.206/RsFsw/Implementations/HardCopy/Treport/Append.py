from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Append:
	"""Append commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("append", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy:TREPort:APPend \n
		Snippet: driver.hardCopy.treport.append.set() \n
		This command adds the current measurement results to the test report. The saved data depends on the items you have
		selected with method RsFsw.HardCopy.Treport.Item.Select.set. \n
		"""
		self._core.io.write(f'HCOPy:TREPort:APPend')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:TREPort:APPend \n
		Snippet: driver.hardCopy.treport.append.set_with_opc() \n
		This command adds the current measurement results to the test report. The saved data depends on the items you have
		selected with method RsFsw.HardCopy.Treport.Item.Select.set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:TREPort:APPend', opc_timeout_ms)
