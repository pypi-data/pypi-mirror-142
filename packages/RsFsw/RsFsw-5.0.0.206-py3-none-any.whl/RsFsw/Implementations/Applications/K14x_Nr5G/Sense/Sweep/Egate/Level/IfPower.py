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
		Snippet: driver.applications.k14Xnr5G.sense.sweep.egate.level.ifPower.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:SWEep:EGATe:LEVel:IFPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LEVel:IFPower \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.egate.level.ifPower.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LEVel:IFPower?')
		return Conversions.str_to_float(response)
