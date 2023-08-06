from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqPower:
	"""IqPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IQPower \n
		Snippet: driver.applications.k149Uwb.trigger.sequence.level.iqPower.set(level = 1.0) \n
		This command defines the magnitude the I/Q data must exceed to cause a trigger event. Note that any RF attenuation or
		preamplification is considered when the trigger level is analyzed. If defined, a reference level offset is also
		considered. \n
			:param level: Range: -130 dBm to 30 dBm, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:IQPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IQPower \n
		Snippet: value: float = driver.applications.k149Uwb.trigger.sequence.level.iqPower.get() \n
		This command defines the magnitude the I/Q data must exceed to cause a trigger event. Note that any RF attenuation or
		preamplification is considered when the trigger level is analyzed. If defined, a reference level offset is also
		considered. \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:IQPower?')
		return Conversions.str_to_float(response)
