from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, band: enums.Band) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND \n
		Snippet: driver.sense.mixer.harmonic.band.set(band = enums.Band.A) \n
		This command selects the external mixer band. The query returns the currently selected band. This command is only
		available if the external mixer is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:param band: KA | Q | U | V | E | W | F | D | G | Y | J | USER Standard waveguide band or user-defined band.
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'SENSe:MIXer:HARMonic:BAND {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Band:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND \n
		Snippet: value: enums.Band = driver.sense.mixer.harmonic.band.get() \n
		This command selects the external mixer band. The query returns the currently selected band. This command is only
		available if the external mixer is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:return: band: KA | Q | U | V | E | W | F | D | G | Y | J | USER Standard waveguide band or user-defined band."""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def preset(self) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.sense.mixer.harmonic.band.preset() \n
		This command restores the preset frequency ranges for the selected standard waveguide band. Note:Changes to the band and
		mixer settings are maintained even after using the [PRESET] function. Use this command to restore the predefined band
		ranges. \n
		"""
		self._core.io.write(f'SENSe:MIXer:HARMonic:BAND:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.sense.mixer.harmonic.band.preset_with_opc() \n
		This command restores the preset frequency ranges for the selected standard waveguide band. Note:Changes to the band and
		mixer settings are maintained even after using the [PRESET] function. Use this command to restore the predefined band
		ranges. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:MIXer:HARMonic:BAND:PRESet', opc_timeout_ms)
