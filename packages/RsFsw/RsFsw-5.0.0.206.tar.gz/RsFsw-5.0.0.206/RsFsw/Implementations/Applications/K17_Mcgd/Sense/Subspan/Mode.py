from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, state: enums.AutoMode) -> None:
		"""SCPI: [SENSe]:SUBSpan:MODE \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.mode.set(state = enums.AutoMode.AUTO) \n
		Defines the frequency subspan mode. \n
			:param state: ON | OFF | AUTO
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoMode)
		self._core.io.write(f'SENSe:SUBSpan:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoMode:
		"""SCPI: [SENSe]:SUBSpan:MODE \n
		Snippet: value: enums.AutoMode = driver.applications.k17Mcgd.sense.subspan.mode.get() \n
		Defines the frequency subspan mode. \n
			:return: state: ON | OFF | AUTO"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
