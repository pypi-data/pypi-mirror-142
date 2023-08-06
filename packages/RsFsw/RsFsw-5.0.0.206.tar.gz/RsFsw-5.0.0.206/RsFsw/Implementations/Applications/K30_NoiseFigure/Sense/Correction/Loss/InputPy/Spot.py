from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spot:
	"""Spot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spot", core, parent)

	def set(self, loss: float) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:SPOT \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.spot.set(loss = 1.0) \n
		This command defines a constant input loss for all measurement points. \n
			:param loss: Range: -999.99 to 999.99, Unit: DB
		"""
		param = Conversions.decimal_value_to_str(loss)
		self._core.io.write(f'SENSe:CORRection:LOSS:INPut:SPOT {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:LOSS:INPut:SPOT \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.loss.inputPy.spot.get() \n
		This command defines a constant input loss for all measurement points. \n
			:return: loss: Range: -999.99 to 999.99, Unit: DB"""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:INPut:SPOT?')
		return Conversions.str_to_float(response)
