from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, hysteresis_lower: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure[:HYSTeresis]:LOWer \n
		Snippet: driver.applications.k70Vsa.sense.adjust.configure.hysteresis.lower.set(hysteresis_lower = 1.0) \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. In order to avoid frequent adaptation due to small changes in the input signal, you
		can define a hysteresis. This setting defines a lower threshold the signal must fall below (compared to the last
		measurement) before the reference level is adapted automatically. \n
			:param hysteresis_lower: Range: 0 dB to 200 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(hysteresis_lower)
		self._core.io.write(f'SENSe:ADJust:CONFigure:HYSTeresis:LOWer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure[:HYSTeresis]:LOWer \n
		Snippet: value: float = driver.applications.k70Vsa.sense.adjust.configure.hysteresis.lower.get() \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. In order to avoid frequent adaptation due to small changes in the input signal, you
		can define a hysteresis. This setting defines a lower threshold the signal must fall below (compared to the last
		measurement) before the reference level is adapted automatically. \n
			:return: hysteresis_lower: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:HYSTeresis:LOWer?')
		return Conversions.str_to_float(response)
