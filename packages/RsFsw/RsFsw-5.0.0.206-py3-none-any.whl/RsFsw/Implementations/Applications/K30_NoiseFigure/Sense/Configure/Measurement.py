from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def set(self, measurement: enums.Temperature) -> None:
		"""SCPI: [SENSe]:CONFigure:MEASurement \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.measurement.set(measurement = enums.Temperature.COLD) \n
		This command selects the type of power measurement to perform next. The command is available for manual measurements
		(see[SENSe:]CONFigure:CONTrol ) . \n
			:param measurement: HOT | COLD COLD Performs the Power (Cold) measurement next. HOT Performs the Power (Hot) measurement next.
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.Temperature)
		self._core.io.write(f'SENSe:CONFigure:MEASurement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Temperature:
		"""SCPI: [SENSe]:CONFigure:MEASurement \n
		Snippet: value: enums.Temperature = driver.applications.k30NoiseFigure.sense.configure.measurement.get() \n
		This command selects the type of power measurement to perform next. The command is available for manual measurements
		(see[SENSe:]CONFigure:CONTrol ) . \n
			:return: measurement: HOT | COLD COLD Performs the Power (Cold) measurement next. HOT Performs the Power (Hot) measurement next."""
		response = self._core.io.query_str(f'SENSe:CONFigure:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.Temperature)
