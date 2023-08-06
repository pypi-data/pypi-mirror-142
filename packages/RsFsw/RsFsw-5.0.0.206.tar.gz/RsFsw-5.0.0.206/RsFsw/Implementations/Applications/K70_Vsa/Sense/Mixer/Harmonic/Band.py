from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def preset(self) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.applications.k70Vsa.sense.mixer.harmonic.band.preset() \n
		This command restores the preset frequency ranges for the selected standard waveguide band. Note:Changes to the band and
		mixer settings are maintained even after using the [PRESET] function. Use this command to restore the predefined band
		ranges. \n
		"""
		self._core.io.write(f'SENSe:MIXer:HARMonic:BAND:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.applications.k70Vsa.sense.mixer.harmonic.band.preset_with_opc() \n
		This command restores the preset frequency ranges for the selected standard waveguide band. Note:Changes to the band and
		mixer settings are maintained even after using the [PRESET] function. Use this command to restore the predefined band
		ranges. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:MIXer:HARMonic:BAND:PRESet', opc_timeout_ms)
