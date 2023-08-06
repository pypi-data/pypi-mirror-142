from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:FREQuency \n
		Snippet: driver.applications.k10Xlte.sense.adjust.frequency.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SENSe:ADJust:FREQuency')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:FREQuency \n
		Snippet: driver.applications.k10Xlte.sense.adjust.frequency.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:FREQuency', opc_timeout_ms)
