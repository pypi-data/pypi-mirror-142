from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Online:
	"""Online commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("online", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:IQ:ONLine \n
		Snippet: driver.applications.k40PhaseNoise.sense.iq.online.set(state = False) \n
		This command turns the I/Q online measurement mode on and off. This mode is available for offset frequencies smaller than
		30 kHz. Note that you have to
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- turn on decimation with [SENSe:]IQ:DECimation
			- select the I/Q FFT mode for the affected half decades with [SENSe:]LIST:BWIDth[:RESolution]:TYPE
			- turn off forward sweep with[SENSe:]SWEep:FORWard \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:IQ:ONLine {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:IQ:ONLine \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.iq.online.get() \n
		This command turns the I/Q online measurement mode on and off. This mode is available for offset frequencies smaller than
		30 kHz. Note that you have to
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- turn on decimation with [SENSe:]IQ:DECimation
			- select the I/Q FFT mode for the affected half decades with [SENSe:]LIST:BWIDth[:RESolution]:TYPE
			- turn off forward sweep with[SENSe:]SWEep:FORWard \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:IQ:ONLine?')
		return Conversions.str_to_bool(response)
