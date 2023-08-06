from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.IfGainModeDdem) -> None:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:MODE \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.equalizer.mode.set(mode = enums.IfGainModeDdem.AVERaging) \n
		Switches between the equalizer modes. For details see 'The equalizer'. \n
			:param mode: NORMal Switches the equalizer on for the next sweep. TRACking Switches the equalizer on; the results of the equalizer in the previous sweep are considered to calculate the new filter. FREeze The filter is no longer changed, the current equalizer values are used for subsequent sweeps. USER A user-defined equalizer loaded from a file is used. AVERaging Switches the equalizer on; the results of the equalizer in all previous sweeps (since the instrument was switched on or the equalizer was reset) are considered to calculate the new filter. To start a new averaging process, use the [SENSe:]DDEMod:EQUalizer:RESet command.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IfGainModeDdem)
		self._core.io.write(f'SENSe:DDEMod:EQUalizer:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IfGainModeDdem:
		"""SCPI: [SENSe]:DDEMod:EQUalizer:MODE \n
		Snippet: value: enums.IfGainModeDdem = driver.applications.k70Vsa.sense.ddemod.equalizer.mode.get() \n
		Switches between the equalizer modes. For details see 'The equalizer'. \n
			:return: mode: NORMal Switches the equalizer on for the next sweep. TRACking Switches the equalizer on; the results of the equalizer in the previous sweep are considered to calculate the new filter. FREeze The filter is no longer changed, the current equalizer values are used for subsequent sweeps. USER A user-defined equalizer loaded from a file is used. AVERaging Switches the equalizer on; the results of the equalizer in all previous sweeps (since the instrument was switched on or the equalizer was reset) are considered to calculate the new filter. To start a new averaging process, use the [SENSe:]DDEMod:EQUalizer:RESet command."""
		response = self._core.io.query_str(f'SENSe:DDEMod:EQUalizer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IfGainModeDdem)
