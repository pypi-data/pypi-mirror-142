from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, sweep_type: enums.SweepTypeNr5G) -> None:
		"""SCPI: [SENSe]:SWEep:TYPE \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.typePy.set(sweep_type = enums.SweepTypeNr5G.AUTO) \n
		No command help available \n
			:param sweep_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(sweep_type, enums.SweepTypeNr5G)
		self._core.io.write(f'SENSe:SWEep:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepTypeNr5G:
		"""SCPI: [SENSe]:SWEep:TYPE \n
		Snippet: value: enums.SweepTypeNr5G = driver.applications.k14Xnr5G.sense.sweep.typePy.get() \n
		No command help available \n
			:return: sweep_type: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepTypeNr5G)
