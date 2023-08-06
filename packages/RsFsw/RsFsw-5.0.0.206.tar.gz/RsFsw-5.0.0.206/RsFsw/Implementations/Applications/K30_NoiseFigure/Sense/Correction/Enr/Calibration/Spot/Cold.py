from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cold:
	"""Cold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cold", core, parent)

	def set(self, temperature: float) -> None:
		"""SCPI: [SENSe]:CORRection:ENR:CALibration:SPOT:COLD \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.calibration.spot.cold.set(temperature = 1.0) \n
		This command defines a constant temperature of a resistor not supplied with power (Tcold) used during calibration.
		The command is available when you have selected a noise source with resistor characteristics with
		[SENSe:]CORRection:ENR:CALibration:TYPE. \n
			:param temperature: Temperature in degrees Kelvin. Unit: K
		"""
		param = Conversions.decimal_value_to_str(temperature)
		self._core.io.write(f'SENSe:CORRection:ENR:CALibration:SPOT:COLD {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:ENR:CALibration:SPOT:COLD \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.enr.calibration.spot.cold.get() \n
		This command defines a constant temperature of a resistor not supplied with power (Tcold) used during calibration.
		The command is available when you have selected a noise source with resistor characteristics with
		[SENSe:]CORRection:ENR:CALibration:TYPE. \n
			:return: temperature: Temperature in degrees Kelvin. Unit: K"""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:CALibration:SPOT:COLD?')
		return Conversions.str_to_float(response)
