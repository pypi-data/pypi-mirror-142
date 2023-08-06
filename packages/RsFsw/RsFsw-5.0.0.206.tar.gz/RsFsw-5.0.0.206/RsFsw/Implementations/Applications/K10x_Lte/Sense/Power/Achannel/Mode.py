from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.ReferenceMode) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:MODE \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.mode.set(mode = enums.ReferenceMode.ABSolute) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ReferenceMode)
		self._core.io.write(f'SENSe:POWer:ACHannel:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceMode:
		"""SCPI: [SENSe]:POWer:ACHannel:MODE \n
		Snippet: value: enums.ReferenceMode = driver.applications.k10Xlte.sense.power.achannel.mode.get() \n
		No command help available \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
