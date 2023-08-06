from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factory:
	"""Factory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factory", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:REVision:FACTory \n
		Snippet: driver.system.revision.factory.set() \n
		Resets the response to the REV? query to the factory default value. For example, after a user string was defined using
		the method RsFsw.System.Revision.String.set command. (REV? query available for HP emulation only, see method RsFsw.System.
		Language.set.) \n
		"""
		self._core.io.write(f'SYSTem:REVision:FACTory')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:REVision:FACTory \n
		Snippet: driver.system.revision.factory.set_with_opc() \n
		Resets the response to the REV? query to the factory default value. For example, after a user string was defined using
		the method RsFsw.System.Revision.String.set command. (REV? query available for HP emulation only, see method RsFsw.System.
		Language.set.) \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:REVision:FACTory', opc_timeout_ms)
