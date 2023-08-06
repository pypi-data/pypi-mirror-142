from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interface:
	"""Interface commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interface", core, parent)

	def set(self, type_py: enums.GeneratorIntfType, generator=repcap.Generator.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator<gen>:INTerface \n
		Snippet: driver.system.communicate.rdevice.generator.interface.set(type_py = enums.GeneratorIntfType.GPIB, generator = repcap.Generator.Default) \n
		Defines the interface used for the connection to the external generator. \n
			:param type_py: GPIB TCPip
			:param generator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Generator')
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.GeneratorIntfType)
		generator_cmd_val = self._cmd_group.get_repcap_cmd_value(generator, repcap.Generator)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:GENerator{generator_cmd_val}:INTerface {param}')

	# noinspection PyTypeChecker
	def get(self, generator=repcap.Generator.Default) -> enums.GeneratorIntfType:
		"""SCPI: SYSTem:COMMunicate:RDEVice:GENerator<gen>:INTerface \n
		Snippet: value: enums.GeneratorIntfType = driver.system.communicate.rdevice.generator.interface.get(generator = repcap.Generator.Default) \n
		Defines the interface used for the connection to the external generator. \n
			:param generator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Generator')
			:return: type_py: GPIB TCPip"""
		generator_cmd_val = self._cmd_group.get_repcap_cmd_value(generator, repcap.Generator)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:GENerator{generator_cmd_val}:INTerface?')
		return Conversions.str_to_scalar_enum(response, enums.GeneratorIntfType)
