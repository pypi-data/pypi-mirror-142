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
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.level.rfPower.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel:RFPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:RFPower \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.level.rfPower.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel:RFPower?')
		return Conversions.str_to_float(response)
