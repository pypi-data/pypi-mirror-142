from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SQUelch:LEVel \n
		Snippet: driver.sense.ademod.squelch.level.set(threshold = 1.0) \n
		This command defines the level threshold below which the demodulated data is set to 0 if squelching is enabled (see
		[SENSe:]ADEMod:SQUelch[:STATe]) . \n
			:param threshold: numeric value The absolute threshold level Range: -150 dBm to 30 dBm
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:ADEMod:SQUelch:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SQUelch:LEVel \n
		Snippet: value: float = driver.sense.ademod.squelch.level.get() \n
		This command defines the level threshold below which the demodulated data is set to 0 if squelching is enabled (see
		[SENSe:]ADEMod:SQUelch[:STATe]) . \n
			:return: threshold: numeric value The absolute threshold level Range: -150 dBm to 30 dBm"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SQUelch:LEVel?')
		return Conversions.str_to_float(response)
