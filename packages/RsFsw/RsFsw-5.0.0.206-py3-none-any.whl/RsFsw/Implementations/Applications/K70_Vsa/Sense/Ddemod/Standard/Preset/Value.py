from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:PRESet[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.preset.value.set() \n
		This command restores the default settings of the currently selected standard. \n
		"""
		self._core.io.write(f'SENSe:DDEMod:STANdard:PRESet:VALue')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:DDEMod:STANdard:PRESet[:VALue] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.standard.preset.value.set_with_opc() \n
		This command restores the default settings of the currently selected standard. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:DDEMod:STANdard:PRESet:VALue', opc_timeout_ms)
