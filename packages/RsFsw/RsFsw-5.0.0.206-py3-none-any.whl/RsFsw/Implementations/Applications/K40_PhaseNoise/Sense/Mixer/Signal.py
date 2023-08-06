from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signal:
	"""Signal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signal", core, parent)

	def set(self, arg_0: enums.State) -> None:
		"""SCPI: [SENSe]:MIXer:SIGNal \n
		Snippet: driver.applications.k40PhaseNoise.sense.mixer.signal.set(arg_0 = enums.State.ALL) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.State)
		self._core.io.write(f'SENSe:MIXer:SIGNal {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.State:
		"""SCPI: [SENSe]:MIXer:SIGNal \n
		Snippet: value: enums.State = driver.applications.k40PhaseNoise.sense.mixer.signal.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:SIGNal?')
		return Conversions.str_to_scalar_enum(response, enums.State)
