from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:UPPer \n
		Snippet: driver.applications.k17Mcgd.sense.adjust.configure.hysteresis.upper.set(value = 1.0) \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. In order to avoid frequent adaptation due to small changes in the input signal, you
		can define a hysteresis. This setting defines an upper threshold the signal must exceed (compared to the last
		measurement) before the reference level is adapted automatically. \n
			:param value: Range: 0 dB to 200 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure:HYSTeresis:UPPer \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.adjust.configure.hysteresis.upper.get() \n
		When the reference level is adjusted automatically using the [SENSe:]ADJust:LEVel command, the internal attenuators and
		the preamplifier are also adjusted. In order to avoid frequent adaptation due to small changes in the input signal, you
		can define a hysteresis. This setting defines an upper threshold the signal must exceed (compared to the last
		measurement) before the reference level is adapted automatically. \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:HYSTeresis:UPPer?')
		return Conversions.str_to_float(response)
