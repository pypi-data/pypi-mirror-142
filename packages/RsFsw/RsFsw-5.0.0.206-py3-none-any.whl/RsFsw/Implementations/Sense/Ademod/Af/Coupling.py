from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, coupling: enums.CouplingTypeA) -> None:
		"""SCPI: [SENSe]:ADEMod:AF:COUPling \n
		Snippet: driver.sense.ademod.af.coupling.set(coupling = enums.CouplingTypeA.AC) \n
		This command selects the coupling of the AF path of the analyzer in the specified window. \n
			:param coupling: AC | DC
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingTypeA)
		self._core.io.write(f'SENSe:ADEMod:AF:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingTypeA:
		"""SCPI: [SENSe]:ADEMod:AF:COUPling \n
		Snippet: value: enums.CouplingTypeA = driver.sense.ademod.af.coupling.get() \n
		This command selects the coupling of the AF path of the analyzer in the specified window. \n
			:return: coupling: AC | DC"""
		response = self._core.io.query_str(f'SENSe:ADEMod:AF:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeA)
