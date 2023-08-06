from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Banalyze:
	"""Banalyze commands group definition. 15 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("banalyze", core, parent)

	@property
	def btype(self):
		"""btype commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_btype'):
			from .Btype import Btype
			self._btype = Btype(self._core, self._cmd_group)
		return self._btype

	@property
	def symbols(self):
		"""symbols commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbols'):
			from .Symbols import Symbols
			self._symbols = Symbols(self._core, self._cmd_group)
		return self._symbols

	@property
	def dbytes(self):
		"""dbytes commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dbytes'):
			from .Dbytes import Dbytes
			self._dbytes = Dbytes(self._core, self._cmd_group)
		return self._dbytes

	@property
	def duration(self):
		"""duration commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	def set(self, format_py: str) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.set(format_py = '1') \n
		Specifies which PSDUs are to be analyzed depending on their modulation. Only PSDUs using the selected modulation are
		considered in result analysis. Note: to analyze all PPDUs that are identical to the first detected PPDU (corresponds to
		'Auto, same type as first PPDU') , use the command: SENS:DEMO:FORM:BANA:BTYP:AUTO:TYPE FBUR. To analyze all PPDUs
		regardless of their format and modulation (corresponds to 'Auto, individually for each PPDU') , use the command:
		SENS:DEMO:FORM:BANA:BTYP:AUTO:TYPE ALL. See [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE. \n
			:param format_py: No help available
		"""
		param = Conversions.value_to_quoted_str(format_py)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze \n
		Snippet: value: str = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.get() \n
		Specifies which PSDUs are to be analyzed depending on their modulation. Only PSDUs using the selected modulation are
		considered in result analysis. Note: to analyze all PPDUs that are identical to the first detected PPDU (corresponds to
		'Auto, same type as first PPDU') , use the command: SENS:DEMO:FORM:BANA:BTYP:AUTO:TYPE FBUR. To analyze all PPDUs
		regardless of their format and modulation (corresponds to 'Auto, individually for each PPDU') , use the command:
		SENS:DEMO:FORM:BANA:BTYP:AUTO:TYPE ALL. See [SENSe:]DEMod:FORMat:BANalyze:BTYPe:AUTO:TYPE. \n
			:return: format_py: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze?')
		return trim_str_response(response)

	def clone(self) -> 'Banalyze':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Banalyze(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
