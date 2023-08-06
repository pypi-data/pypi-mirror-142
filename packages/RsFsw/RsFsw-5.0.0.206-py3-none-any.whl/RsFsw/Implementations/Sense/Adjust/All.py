from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:ALL \n
		Snippet: driver.sense.adjust.all.set() \n
		This command initiates a measurement to determine and set the ideal settings for the current task automatically (only
		once for the current measurement) . This includes:
			- Center frequency
			- Reference level
			- Scaling \n
		"""
		self._core.io.write(f'SENSe:ADJust:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:ALL \n
		Snippet: driver.sense.adjust.all.set_with_opc() \n
		This command initiates a measurement to determine and set the ideal settings for the current task automatically (only
		once for the current measurement) . This includes:
			- Center frequency
			- Reference level
			- Scaling \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:ALL', opc_timeout_ms)
