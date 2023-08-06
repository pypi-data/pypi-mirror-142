from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def eauto(self):
		"""eauto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eauto'):
			from .Eauto import Eauto
			self._eauto = Eauto(self._core, self._cmd_group)
		return self._eauto

	def set(self, source: enums.ReferenceSourceA) -> None:
		"""SCPI: [SENSe]:ROSCillator:SOURce \n
		Snippet: driver.sense.roscillator.source.set(source = enums.ReferenceSourceA.E10) \n
		This command selects the reference oscillator. If you want to select the external reference, it must be connected to the
		R&S FSW. \n
			:param source: INTernal The internal reference is used (10 MHz) . EXTernal | EXTernal1 | EXT1 The external reference from the 'REF INPUT 10 MHZ' connector is used; if none is available, an error flag is displayed in the status bar. E10 The external reference from 'REF INPUT 1..50 MHZ' connector is used with a fixed 10 MHZ frequency; if none is available, an error flag is displayed in the status bar. E100 The external reference from the 'REF INPUT 100 MHZ / 1 GHz' connector is used with a fixed 100 MHZ frequency; if none is available, an error flag is displayed in the status bar. E1000 The external reference from 'REF INPUT 100 MHZ / 1 GHz' connector is used with a fixed 1 GHZ frequency; if none is available, an error flag is displayed in the status bar. EAUTo The external reference is used as long as it is available, then the instrument switches to the internal reference. SYNC The external reference is used; if none is available, an error flag is displayed in the status bar.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ReferenceSourceA)
		self._core.io.write(f'SENSe:ROSCillator:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ReferenceSourceA:
		"""SCPI: [SENSe]:ROSCillator:SOURce \n
		Snippet: value: enums.ReferenceSourceA = driver.sense.roscillator.source.get() \n
		This command selects the reference oscillator. If you want to select the external reference, it must be connected to the
		R&S FSW. \n
			:return: source: INTernal The internal reference is used (10 MHz) . EXTernal | EXTernal1 | EXT1 The external reference from the 'REF INPUT 10 MHZ' connector is used; if none is available, an error flag is displayed in the status bar. E10 The external reference from 'REF INPUT 1..50 MHZ' connector is used with a fixed 10 MHZ frequency; if none is available, an error flag is displayed in the status bar. E100 The external reference from the 'REF INPUT 100 MHZ / 1 GHz' connector is used with a fixed 100 MHZ frequency; if none is available, an error flag is displayed in the status bar. E1000 The external reference from 'REF INPUT 100 MHZ / 1 GHz' connector is used with a fixed 1 GHZ frequency; if none is available, an error flag is displayed in the status bar. EAUTo The external reference is used as long as it is available, then the instrument switches to the internal reference. SYNC The external reference is used; if none is available, an error flag is displayed in the status bar."""
		response = self._core.io.query_str(f'SENSe:ROSCillator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceSourceA)

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
