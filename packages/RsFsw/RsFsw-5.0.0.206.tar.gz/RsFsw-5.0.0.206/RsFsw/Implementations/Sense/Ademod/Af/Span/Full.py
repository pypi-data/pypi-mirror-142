from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Full:
	"""Full commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("full", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADEMod:AF:SPAN:FULL \n
		Snippet: driver.sense.ademod.af.span.full.set() \n
		This command sets the maximum span for AF spectrum result display. The maximum span corresponds to DBW/2 (see
		[SENSe:]BWIDth:DEMod) . \n
		"""
		self._core.io.write(f'SENSe:ADEMod:AF:SPAN:FULL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADEMod:AF:SPAN:FULL \n
		Snippet: driver.sense.ademod.af.span.full.set_with_opc() \n
		This command sets the maximum span for AF spectrum result display. The maximum span corresponds to DBW/2 (see
		[SENSe:]BWIDth:DEMod) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADEMod:AF:SPAN:FULL', opc_timeout_ms)
