from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel:ALL \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.level.all.set() \n
		This command determines the ideal reference level based on the current measurement data and settings on all connected
		input sources. This ensures that the settings of the RF attenuation and the reference level are optimally adjusted to the
		signal level without overloading the R&S FSW or limiting the dynamic range by an S/N ratio that is too small. The command
		is available for MIMO measurements with more than one input source. \n
		"""
		self._core.io.write(f'SENSe:ADJust:LEVel:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:LEVel:ALL \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.level.all.set_with_opc() \n
		This command determines the ideal reference level based on the current measurement data and settings on all connected
		input sources. This ensures that the settings of the RF attenuation and the reference level are optimally adjusted to the
		signal level without overloading the R&S FSW or limiting the dynamic range by an S/N ratio that is too small. The command
		is available for MIMO measurements with more than one input source. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:LEVel:ALL', opc_timeout_ms)
