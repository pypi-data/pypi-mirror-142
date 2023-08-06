from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soffset:
	"""Soffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soffset", core, parent)

	def set(self, sensor_offset: float) -> None:
		"""SCPI: [SENSe]:PMETer:SOFFset \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.soffset.set(sensor_offset = 1.0) \n
		Takes the specified offset into account for the measured power. Only available if [SENSe:]PMETer{p}:ROFFset[:STATe] is
		disabled. \n
			:param sensor_offset: Unit: DB
		"""
		param = Conversions.decimal_value_to_str(sensor_offset)
		self._core.io.write(f'SENSe:PMETer:SOFFset {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:SOFFset \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.soffset.get() \n
		Takes the specified offset into account for the measured power. Only available if [SENSe:]PMETer{p}:ROFFset[:STATe] is
		disabled. \n
			:return: sensor_offset: Unit: DB"""
		response = self._core.io.query_str(f'SENSe:PMETer:SOFFset?')
		return Conversions.str_to_float(response)
