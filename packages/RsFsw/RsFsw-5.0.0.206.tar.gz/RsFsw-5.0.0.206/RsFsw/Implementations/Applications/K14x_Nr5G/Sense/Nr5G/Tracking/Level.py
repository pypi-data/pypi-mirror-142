from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:TRACking:LEVel \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.tracking.level.set(state = False) \n
		This command turns level tracking on and off. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:TRACking:LEVel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:TRACking:LEVel \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.tracking.level.get() \n
		This command turns level tracking on and off. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:NR5G:TRACking:LEVel?')
		return Conversions.str_to_bool(response)
