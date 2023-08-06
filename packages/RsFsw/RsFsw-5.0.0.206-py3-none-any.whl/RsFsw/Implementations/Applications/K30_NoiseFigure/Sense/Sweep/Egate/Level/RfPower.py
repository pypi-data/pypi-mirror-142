from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPower:
	"""RfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:RFPower \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.level.rfPower.set(level = 1.0) \n
		Defines the gate level for which the gate is open. Note that any RF attenuation or preamplification is considered when
		the trigger level is analyzed. If defined, a reference level offset is also considered. The input signal must be between
		500 MHz and 8 GHz. This command is only available for triggered gated measurements ([SENSe:]SWEep:EGATe:AUTOMAN) . \n
			:param level: For details on available trigger levels and trigger bandwidths see the data sheet. Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel:RFPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:RFPower \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.egate.level.rfPower.get() \n
		Defines the gate level for which the gate is open. Note that any RF attenuation or preamplification is considered when
		the trigger level is analyzed. If defined, a reference level offset is also considered. The input signal must be between
		500 MHz and 8 GHz. This command is only available for triggered gated measurements ([SENSe:]SWEep:EGATe:AUTOMAN) . \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel:RFPower?')
		return Conversions.str_to_float(response)
