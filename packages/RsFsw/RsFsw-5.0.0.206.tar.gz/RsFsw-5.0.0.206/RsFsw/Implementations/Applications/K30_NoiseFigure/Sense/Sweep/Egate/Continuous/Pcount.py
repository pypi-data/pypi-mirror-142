from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcount:
	"""Pcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcount", core, parent)

	def set(self, amount: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PCOunt \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.continuous.pcount.set(amount = 1.0) \n
		Defines the number of gate periods to be measured after a single trigger event. \n
			:param amount: integer Range: 1 to 1023
		"""
		param = Conversions.decimal_value_to_str(amount)
		self._core.io.write(f'SENSe:SWEep:EGATe:CONTinuous:PCOunt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PCOunt \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.egate.continuous.pcount.get() \n
		Defines the number of gate periods to be measured after a single trigger event. \n
			:return: amount: integer Range: 1 to 1023"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:CONTinuous:PCOunt?')
		return Conversions.str_to_float(response)
