from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, ser_level: float) -> None:
		"""SCPI: [SENSe]:DDEMod:FSYNc:LEVel \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.fsync.level.set(ser_level = 1.0) \n
		This command sets the Fine Sync Level if fine sync works on Known Data \n
			:param ser_level: Range: 0.0 to 100.0, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(ser_level)
		self._core.io.write(f'SENSe:DDEMod:FSYNc:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:FSYNc:LEVel \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.fsync.level.get() \n
		This command sets the Fine Sync Level if fine sync works on Known Data \n
			:return: ser_level: Range: 0.0 to 100.0, Unit: PCT"""
		response = self._core.io.query_str(f'SENSe:DDEMod:FSYNc:LEVel?')
		return Conversions.str_to_float(response)
