from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefMeas:
	"""RefMeas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refMeas", core, parent)

	def set(self) -> None:
		"""SCPI: INITiate:REFMeas \n
		Snippet: driver.applications.k70Vsa.initiate.refMeas.set() \n
		Repeats the evaluation of the data currently in the capture buffer without capturing new data. This is useful for long
		capture buffers that are split into sections for result displays. In this case, only the data in the currently selected
		capture buffer section is automatically refreshed after configuration changes. To update the entire capture buffer, you
		must refresh the evaluation manually using this command. See also 'Capture buffer display'. \n
		"""
		self._core.io.write(f'INITiate:REFMeas')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:REFMeas \n
		Snippet: driver.applications.k70Vsa.initiate.refMeas.set_with_opc() \n
		Repeats the evaluation of the data currently in the capture buffer without capturing new data. This is useful for long
		capture buffers that are split into sections for result displays. In this case, only the data in the currently selected
		capture buffer section is automatically refreshed after configuration changes. To update the entire capture buffer, you
		must refresh the evaluation manually using this command. See also 'Capture buffer display'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:REFMeas', opc_timeout_ms)
