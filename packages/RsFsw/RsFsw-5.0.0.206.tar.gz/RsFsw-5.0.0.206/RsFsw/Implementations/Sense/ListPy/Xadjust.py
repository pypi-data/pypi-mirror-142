from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Xadjust:
	"""Xadjust commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xadjust", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:LIST:XADJust \n
		Snippet: driver.sense.listPy.xadjust.set() \n
		Sets the x-axis range for the spurious emission measurement from the start frequency of the first sweep range to the stop
		frequency of the last sweep range. \n
		"""
		self._core.io.write(f'SENSe:LIST:XADJust')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:LIST:XADJust \n
		Snippet: driver.sense.listPy.xadjust.set_with_opc() \n
		Sets the x-axis range for the spurious emission measurement from the start frequency of the first sweep range to the stop
		frequency of the last sweep range. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:LIST:XADJust', opc_timeout_ms)
