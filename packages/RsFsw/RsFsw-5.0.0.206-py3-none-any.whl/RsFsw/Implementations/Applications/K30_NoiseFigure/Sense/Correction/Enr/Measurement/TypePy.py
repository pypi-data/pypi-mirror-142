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

	def set(self, type_py: enums.EnrType) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TYPE \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.typePy.set(type_py = enums.EnrType.DIODe) \n
		This command selects the type of noise source you are using for the measurement. \n
			:param type_py: DIODe Selects a noise source with diode characteristics. RESistor Selects a noise source with resistor characteristics. When you select this noise source type, the application automatically selects the manual measurement mode (see [SENSe:]CONFigure:CONTrol) . SMARt Selects a smart noise source.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.EnrType)
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EnrType:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TYPE \n
		Snippet: value: enums.EnrType = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.typePy.get() \n
		This command selects the type of noise source you are using for the measurement. \n
			:return: type_py: DIODe Selects a noise source with diode characteristics. RESistor Selects a noise source with resistor characteristics. When you select this noise source type, the application automatically selects the manual measurement mode (see [SENSe:]CONFigure:CONTrol) . SMARt Selects a smart noise source."""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:MEASurement:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.EnrType)
