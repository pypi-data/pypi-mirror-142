from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class New:
	"""New commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("new", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy:TREPort:NEW \n
		Snippet: driver.hardCopy.treport.new.set() \n
		This command creates a new dataset for a new test report. Creating a new test report deletes all previously saved
		datasets. The current measurement results are added as the first dataset to the new report. The R&S FSW saves the data
		selected with method RsFsw.HardCopy.Treport.Item.Select.set. To save the report, use method RsFsw.HardCopy.Immediate.set. \n
		"""
		self._core.io.write(f'HCOPy:TREPort:NEW')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:TREPort:NEW \n
		Snippet: driver.hardCopy.treport.new.set_with_opc() \n
		This command creates a new dataset for a new test report. Creating a new test report deletes all previously saved
		datasets. The current measurement results are added as the first dataset to the new report. The R&S FSW saves the data
		selected with method RsFsw.HardCopy.Treport.Item.Select.set. To save the report, use method RsFsw.HardCopy.Immediate.set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:TREPort:NEW', opc_timeout_ms)
