from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoComp:
	"""LoComp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loComp", core, parent)

	def set(self, loc_state: bool) -> None:
		"""SCPI: [SENSe]:CESTimation:LOComp \n
		Snippet: driver.applications.k17Mcgd.sense.cestimation.loComp.set(loc_state = False) \n
		This command enables or disables the Large Offset Compensation. \n
			:param loc_state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(loc_state)
		self._core.io.write(f'SENSe:CESTimation:LOComp {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CESTimation:LOComp \n
		Snippet: value: bool = driver.applications.k17Mcgd.sense.cestimation.loComp.get() \n
		This command enables or disables the Large Offset Compensation. \n
			:return: loc_state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SENSe:CESTimation:LOComp?')
		return Conversions.str_to_bool(response)
