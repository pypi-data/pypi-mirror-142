from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Traces:
	"""Traces commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("traces", core, parent)

	def set(self, selection: enums.SelectionScope) -> None:
		"""SCPI: FORMat:DIMPort:TRACes \n
		Snippet: driver.applications.k40PhaseNoise.formatPy.dimport.traces.set(selection = enums.SelectionScope.ALL) \n
		This command selects the data to be included in a data import file (see method RsFsw.MassMemory.Load.Trace.set) . \n
			:param selection: SINGle | ALL SINGle Only a single trace is selected for import, namely the one specified by the method RsFsw.MassMemory.Load.Trace.set command. ALL Imports several traces at once, overwriting the existing trace data for any active trace in the result display with the same trace number. Data from the import file for currently not active traces is not imported. The trace parameter for the method RsFsw.MassMemory.Load.Trace.set command is ignored.
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.SelectionScope)
		self._core.io.write(f'FORMat:DIMPort:TRACes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SelectionScope:
		"""SCPI: FORMat:DIMPort:TRACes \n
		Snippet: value: enums.SelectionScope = driver.applications.k40PhaseNoise.formatPy.dimport.traces.get() \n
		This command selects the data to be included in a data import file (see method RsFsw.MassMemory.Load.Trace.set) . \n
			:return: selection: SINGle | ALL SINGle Only a single trace is selected for import, namely the one specified by the method RsFsw.MassMemory.Load.Trace.set command. ALL Imports several traces at once, overwriting the existing trace data for any active trace in the result display with the same trace number. Data from the import file for currently not active traces is not imported. The trace parameter for the method RsFsw.MassMemory.Load.Trace.set command is ignored."""
		response = self._core.io.query_str(f'FORMat:DIMPort:TRACes?')
		return Conversions.str_to_scalar_enum(response, enums.SelectionScope)
