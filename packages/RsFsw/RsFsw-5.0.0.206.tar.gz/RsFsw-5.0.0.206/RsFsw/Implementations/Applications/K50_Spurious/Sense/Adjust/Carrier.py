from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:CARRier \n
		Snippet: driver.applications.k50Spurious.sense.adjust.carrier.set() \n
		Automatically detects the highest peak over the complete frequency range of the analyzer. This value is considered to be
		the reference carrier and is indicated in 'Carrier Level'. \n
		"""
		self._core.io.write(f'SENSe:ADJust:CARRier')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:CARRier \n
		Snippet: driver.applications.k50Spurious.sense.adjust.carrier.set_with_opc() \n
		Automatically detects the highest peak over the complete frequency range of the analyzer. This value is considered to be
		the reference carrier and is indicated in 'Carrier Level'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:CARRier', opc_timeout_ms)
