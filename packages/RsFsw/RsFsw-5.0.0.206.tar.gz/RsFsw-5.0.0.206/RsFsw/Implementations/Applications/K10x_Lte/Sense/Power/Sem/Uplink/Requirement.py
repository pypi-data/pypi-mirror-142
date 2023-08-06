from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Requirement:
	"""Requirement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("requirement", core, parent)

	def set(self, requirement: enums.SemRequirement) -> None:
		"""SCPI: [SENSe]:POWer:SEM:UL:REQuirement \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.uplink.requirement.set(requirement = enums.SemRequirement.GEN) \n
		This command selects the requirements for a spectrum emission mask. \n
			:param requirement: GEN General spectrum emission mask. NS3 | NS4 | NS67 | NS27 | NS35 Spectrum emission masks with additional requirements.
		"""
		param = Conversions.enum_scalar_to_str(requirement, enums.SemRequirement)
		self._core.io.write(f'SENSe:POWer:SEM:UL:REQuirement {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SemRequirement:
		"""SCPI: [SENSe]:POWer:SEM:UL:REQuirement \n
		Snippet: value: enums.SemRequirement = driver.applications.k10Xlte.sense.power.sem.uplink.requirement.get() \n
		This command selects the requirements for a spectrum emission mask. \n
			:return: requirement: GEN General spectrum emission mask. NS3 | NS4 | NS67 | NS27 | NS35 Spectrum emission masks with additional requirements."""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:UL:REQuirement?')
		return Conversions.str_to_scalar_enum(response, enums.SemRequirement)
