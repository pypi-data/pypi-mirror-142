from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: SOURce:EXTernal:POWer[:LEVel] \n
		Snippet: driver.applications.k30NoiseFigure.source.external.power.level.set(level = 1.0) \n
		This command sets the output power of the selected generator. This command is only valid if External Generator Control
		(R&S FSW-B10) is installed and active. \n
			:param level: numeric value Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce:EXTernal:POWer:LEVel {param}')

	def get(self) -> float:
		"""SCPI: SOURce:EXTernal:POWer[:LEVel] \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.external.power.level.get() \n
		This command sets the output power of the selected generator. This command is only valid if External Generator Control
		(R&S FSW-B10) is installed and active. \n
			:return: level: numeric value Unit: DBM"""
		response = self._core.io.query_str(f'SOURce:EXTernal:POWer:LEVel?')
		return Conversions.str_to_float(response)
