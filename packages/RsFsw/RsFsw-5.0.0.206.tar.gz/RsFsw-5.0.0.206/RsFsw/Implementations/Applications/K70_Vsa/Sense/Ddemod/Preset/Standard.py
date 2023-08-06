from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, standard: enums.TechnologyStandardDdem) -> None:
		"""SCPI: [SENSe]:DDEMod:PRESet[:STANdard] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.preset.standard.set(standard = enums.TechnologyStandardDdem.DECT) \n
		This command selects an automatic setting of all modulation parameters according to a standardized transmission method or
		a user-defined transmission method. The standardized transmission methods are available in the instrument as predefined
		standards. \n
			:param standard: (enum or string) Specifies the file name that contains the transmission method without the extension. For user-defined standards, the file path must be included. Default standards predefined by Rohde&Schwarz do not require a path definition. A list of predefined standards (including short forms) is provided in the annex (see 'Predefined standards and settings') .
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.TechnologyStandardDdem)
		self._core.io.write(f'SENSe:DDEMod:PRESet:STANdard {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TechnologyStandardDdem:
		"""SCPI: [SENSe]:DDEMod:PRESet[:STANdard] \n
		Snippet: value: enums.TechnologyStandardDdem = driver.applications.k70Vsa.sense.ddemod.preset.standard.get() \n
		This command selects an automatic setting of all modulation parameters according to a standardized transmission method or
		a user-defined transmission method. The standardized transmission methods are available in the instrument as predefined
		standards. \n
			:return: standard: (enum or string) Specifies the file name that contains the transmission method without the extension. For user-defined standards, the file path must be included. Default standards predefined by Rohde&Schwarz do not require a path definition. A list of predefined standards (including short forms) is provided in the annex (see 'Predefined standards and settings') ."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PRESet:STANdard?')
		return Conversions.str_to_scalar_enum_ext(response, enums.TechnologyStandardDdem)
