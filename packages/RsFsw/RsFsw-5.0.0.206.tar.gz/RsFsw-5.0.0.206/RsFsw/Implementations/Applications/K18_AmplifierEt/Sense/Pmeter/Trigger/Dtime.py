from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dtime:
	"""Dtime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtime", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:PMETer:TRIGger:DTIMe \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.trigger.dtime.set(time = 1.0) \n
		This command defines the time period that the input signal has to stay below the IF power trigger level before the
		measurement starts. \n
			:param time: Range: 0 s to 1 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:PMETer:TRIGger:DTIMe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:TRIGger:DTIMe \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.trigger.dtime.get() \n
		This command defines the time period that the input signal has to stay below the IF power trigger level before the
		measurement starts. \n
			:return: time: Range: 0 s to 1 s, Unit: S"""
		response = self._core.io.query_str(f'SENSe:PMETer:TRIGger:DTIMe?')
		return Conversions.str_to_float(response)
