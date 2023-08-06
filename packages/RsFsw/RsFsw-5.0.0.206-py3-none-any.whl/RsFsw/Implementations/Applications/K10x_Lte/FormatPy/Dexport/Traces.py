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
		"""SCPI: FORMat:DEXPort:TRACes \n
		Snippet: driver.applications.k10Xlte.formatPy.dexport.traces.set(selection = enums.SelectionScope.ALL) \n
		This command selects the data to be included in a data export file (see method RsFsw.MassMemory.Store.Trace.set) . \n
			:param selection: SINGle | ALL SINGle Only a single trace is selected for export, namely the one specified by the method RsFsw.MassMemory.Store.Trace.set command. ALL Selects all active traces and result tables (e.g. Result Summary, marker peak list etc.) in the current application for export to an ASCII file. The trace parameter for the method RsFsw.MassMemory.Store.Trace.set command is ignored.
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.SelectionScope)
		self._core.io.write(f'FORMat:DEXPort:TRACes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SelectionScope:
		"""SCPI: FORMat:DEXPort:TRACes \n
		Snippet: value: enums.SelectionScope = driver.applications.k10Xlte.formatPy.dexport.traces.get() \n
		This command selects the data to be included in a data export file (see method RsFsw.MassMemory.Store.Trace.set) . \n
			:return: selection: SINGle | ALL SINGle Only a single trace is selected for export, namely the one specified by the method RsFsw.MassMemory.Store.Trace.set command. ALL Selects all active traces and result tables (e.g. Result Summary, marker peak list etc.) in the current application for export to an ASCII file. The trace parameter for the method RsFsw.MassMemory.Store.Trace.set command is ignored."""
		response = self._core.io.query_str(f'FORMat:DEXPort:TRACes?')
		return Conversions.str_to_scalar_enum(response, enums.SelectionScope)
