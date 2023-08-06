from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PreSelection:
	"""PreSelection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preSelection", core, parent)

	def set(self) -> None:
		"""SCPI: CALibration:PRESelection \n
		Snippet: driver.calibration.preSelection.set() \n
		Due to changes in temperature, the YIG-preselector frequency may become slightly offset. This command re-aligns the
		preselector quickly, without requiring a full self-alignment of the R&S FSW. This command is only available for R&S FSW
		models 1331.5003Kxx, and only if a YIG-preselector is available. \n
		"""
		self._core.io.write(f'CALibration:PRESelection')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:PRESelection \n
		Snippet: driver.calibration.preSelection.set_with_opc() \n
		Due to changes in temperature, the YIG-preselector frequency may become slightly offset. This command re-aligns the
		preselector quickly, without requiring a full self-alignment of the R&S FSW. This command is only available for R&S FSW
		models 1331.5003Kxx, and only if a YIG-preselector is available. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:PRESelection', opc_timeout_ms)
