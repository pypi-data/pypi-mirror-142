from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def set(self, hysteresis: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:IFPower:HYSTeresis \n
		Snippet: driver.applications.k9X11Ad.trigger.sequence.ifPower.hysteresis.set(hysteresis = 1.0) \n
		This command defines the trigger hysteresis, which is only available for 'IF Power' trigger sources. \n
			:param hysteresis: Range: 3 dB to 50 dB, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		self._core.io.write(f'TRIGger:SEQuence:IFPower:HYSTeresis {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:IFPower:HYSTeresis \n
		Snippet: value: float = driver.applications.k9X11Ad.trigger.sequence.ifPower.hysteresis.get() \n
		This command defines the trigger hysteresis, which is only available for 'IF Power' trigger sources. \n
			:return: hysteresis: Range: 3 dB to 50 dB, Unit: DB"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:IFPower:HYSTeresis?')
		return Conversions.str_to_float(response)
