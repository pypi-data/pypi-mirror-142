from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lo:
	"""Lo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lo", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def set(self, lo_type: enums.LoType) -> None:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:LO \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.mode.system.lo.set(lo_type = enums.LoType.FIXed) \n
		This command selects the type of local oscillator you are using. The command is available for measurements on frequency
		converting DUTs [SENSe:]CONFigure:MODE:DUT . \n
			:param lo_type: FIXed | VARiable FIXed The local oscillator is used as a fixed frequency source. The IF is variable. VARiable The local oscillator is used as a variable frequency source. The IF is fixed.
		"""
		param = Conversions.enum_scalar_to_str(lo_type, enums.LoType)
		self._core.io.write(f'SENSe:CONFigure:MODE:SYSTem:LO {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LoType:
		"""SCPI: [SENSe]:CONFigure:MODE:SYSTem:LO \n
		Snippet: value: enums.LoType = driver.applications.k30NoiseFigure.sense.configure.mode.system.lo.get() \n
		This command selects the type of local oscillator you are using. The command is available for measurements on frequency
		converting DUTs [SENSe:]CONFigure:MODE:DUT . \n
			:return: lo_type: FIXed | VARiable FIXed The local oscillator is used as a fixed frequency source. The IF is variable. VARiable The local oscillator is used as a variable frequency source. The IF is fixed."""
		response = self._core.io.query_str(f'SENSe:CONFigure:MODE:SYSTem:LO?')
		return Conversions.str_to_scalar_enum(response, enums.LoType)

	def clone(self) -> 'Lo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
