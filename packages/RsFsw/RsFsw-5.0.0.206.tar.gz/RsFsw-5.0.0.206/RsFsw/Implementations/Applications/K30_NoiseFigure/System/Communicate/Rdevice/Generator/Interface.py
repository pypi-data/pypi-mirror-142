from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interface:
	"""Interface commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interface", core, parent)

	def set(self, type_py: enums.GeneratorIntf) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:INTerface \n
		Snippet: driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.interface.set(type_py = enums.GeneratorIntf.GPIB) \n
		Defines the interface used for the connection to the external generator. \n
			:param type_py: GPIB TCPip
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.GeneratorIntf)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:GENerator:INTerface {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.GeneratorIntf:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator:INTerface \n
		Snippet: value: enums.GeneratorIntf = driver.applications.k30NoiseFigure.system.communicate.rdevice.generator.interface.get() \n
		Defines the interface used for the connection to the external generator. \n
			:return: type_py: GPIB TCPip"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:GENerator:INTerface?')
		return Conversions.str_to_scalar_enum(response, enums.GeneratorIntf)
