from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.IfGainMode) -> None:
		"""SCPI: SYSTem:IFGain:MODE \n
		Snippet: driver.system.ifGain.mode.set(mode = enums.IfGainMode.NORMal) \n
		Configures the internal IF gain settings in HP emulation mode due to the application needs. This setting is only taken
		into account for resolution bandwidth < 300 kHz and is only available if a HP language is selected using method RsFsw.
		System.Language.set. \n
			:param mode: NORMal | PULSe NORMal Optimized for high dynamic range, overload limit is close to reference level. PULSe Optimized for pulsed signals, overload limit up to 10 dB above reference level.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.IfGainMode)
		self._core.io.write(f'SYSTem:IFGain:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IfGainMode:
		"""SCPI: SYSTem:IFGain:MODE \n
		Snippet: value: enums.IfGainMode = driver.system.ifGain.mode.get() \n
		Configures the internal IF gain settings in HP emulation mode due to the application needs. This setting is only taken
		into account for resolution bandwidth < 300 kHz and is only available if a HP language is selected using method RsFsw.
		System.Language.set. \n
			:return: mode: NORMal | PULSe NORMal Optimized for high dynamic range, overload limit is close to reference level. PULSe Optimized for pulsed signals, overload limit up to 10 dB above reference level."""
		response = self._core.io.query_str(f'SYSTem:IFGain:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.IfGainMode)
