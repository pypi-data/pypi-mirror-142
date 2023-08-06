from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPower:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: driver.applications.k17Mcgd.trigger.sequence.level.ifPower.set(level = 1.0) \n
		This command defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event.
		Note that any RF attenuation or preamplification is considered when the trigger level is analyzed.
		If defined, a reference level offset is also considered. \n
			:param level: For details on available trigger levels and trigger bandwidths see the data sheet. Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:IFPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: value: float = driver.applications.k17Mcgd.trigger.sequence.level.ifPower.get() \n
		This command defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event.
		Note that any RF attenuation or preamplification is considered when the trigger level is analyzed.
		If defined, a reference level offset is also considered. \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:IFPower?')
		return Conversions.str_to_float(response)
