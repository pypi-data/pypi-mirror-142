from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Roscillator:
	"""Roscillator commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roscillator", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, source: enums.SourceInt) -> None:
		"""SCPI: CONFigure:GENerator:EXTernal:ROSCillator \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.external.roscillator.set(source = enums.SourceInt.EXTernal) \n
		This command selects the source of the generator reference frequency. Make sure to synchronize with *OPC? or *WAI to make
		sure that the command was successfully applied on the generator before sending the next command. \n
			:param source: EXT The generator uses an external reference frequency (for example that of the R&S FSW) . INT The generator uses its own (internal) reference frequency.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'CONFigure:GENerator:EXTernal:ROSCillator {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceInt:
		"""SCPI: CONFigure:GENerator:EXTernal:ROSCillator \n
		Snippet: value: enums.SourceInt = driver.applications.k18AmplifierEt.configure.generator.external.roscillator.get() \n
		This command selects the source of the generator reference frequency. Make sure to synchronize with *OPC? or *WAI to make
		sure that the command was successfully applied on the generator before sending the next command. \n
			:return: source: EXT The generator uses an external reference frequency (for example that of the R&S FSW) . INT The generator uses its own (internal) reference frequency."""
		response = self._core.io.query_str(f'CONFigure:GENerator:EXTernal:ROSCillator?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def clone(self) -> 'Roscillator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Roscillator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
