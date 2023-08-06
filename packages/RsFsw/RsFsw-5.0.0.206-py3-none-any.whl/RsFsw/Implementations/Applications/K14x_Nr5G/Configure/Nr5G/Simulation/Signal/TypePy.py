from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, arg_0: enums.SignalSource) -> None:
		"""SCPI: CONFigure[:NR5G]:SIMulation:SIGNal:TYPE \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.simulation.signal.typePy.set(arg_0 = enums.SignalSource.INSTrument) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.SignalSource)
		self._core.io.write(f'CONFigure:NR5G:SIMulation:SIGNal:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalSource:
		"""SCPI: CONFigure[:NR5G]:SIMulation:SIGNal:TYPE \n
		Snippet: value: enums.SignalSource = driver.applications.k14Xnr5G.configure.nr5G.simulation.signal.typePy.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:SIMulation:SIGNal:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSource)
