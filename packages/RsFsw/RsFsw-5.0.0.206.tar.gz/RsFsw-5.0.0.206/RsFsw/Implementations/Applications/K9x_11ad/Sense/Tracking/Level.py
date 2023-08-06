from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:TRACking:LEVel \n
		Snippet: driver.applications.k9X11Ad.sense.tracking.level.set(state = False) \n
		Activates or deactivates the compensation for level variations within a single PPDU. If activated, the measurement
		results are compensated for level error on a per-symbol basis. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:TRACking:LEVel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:TRACking:LEVel \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.tracking.level.get() \n
		Activates or deactivates the compensation for level variations within a single PPDU. If activated, the measurement
		results are compensated for level error on a per-symbol basis. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:TRACking:LEVel?')
		return Conversions.str_to_bool(response)
