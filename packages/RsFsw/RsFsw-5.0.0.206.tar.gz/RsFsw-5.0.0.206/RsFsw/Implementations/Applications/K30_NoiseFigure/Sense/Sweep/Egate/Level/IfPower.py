from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPower:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:IFPower \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.level.ifPower.set(level = 1.0) \n
		Defines the the power level at the third intermediate frequency that must be exceeded for the gate to be open. Note that
		any RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level
		offset is also considered. This command is only available for triggered gated measurements ([SENSe:]SWEep:EGATe:AUTOMAN) . \n
			:param level: For details on available trigger levels and trigger bandwidths see the data sheet. Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel:IFPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:IFPower \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.egate.level.ifPower.get() \n
		Defines the the power level at the third intermediate frequency that must be exceeded for the gate to be open. Note that
		any RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level
		offset is also considered. This command is only available for triggered gated measurements ([SENSe:]SWEep:EGATe:AUTOMAN) . \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel:IFPower?')
		return Conversions.str_to_float(response)
