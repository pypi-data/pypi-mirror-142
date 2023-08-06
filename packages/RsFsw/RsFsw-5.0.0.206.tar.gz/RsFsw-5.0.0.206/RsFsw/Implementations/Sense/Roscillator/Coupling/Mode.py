from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, state: enums.AutoMode) -> None:
		"""SCPI: [SENSe]:ROSCillator:COUPling:MODE \n
		Snippet: driver.sense.roscillator.coupling.mode.set(state = enums.AutoMode.AUTO) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoMode)
		self._core.io.write(f'SENSe:ROSCillator:COUPling:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoMode:
		"""SCPI: [SENSe]:ROSCillator:COUPling:MODE \n
		Snippet: value: enums.AutoMode = driver.sense.roscillator.coupling.mode.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:ROSCillator:COUPling:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
