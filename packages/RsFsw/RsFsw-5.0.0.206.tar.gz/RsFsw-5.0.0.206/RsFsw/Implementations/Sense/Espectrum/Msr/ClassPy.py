from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ClassPy:
	"""ClassPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("classPy", core, parent)

	def set(self, class_py: enums.RangeClass, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:CLASs \n
		Snippet: driver.sense.espectrum.msr.classPy.set(class_py = enums.RangeClass.LOCal, subBlock = repcap.SubBlock.Default) \n
		Defines the class of the base station according to its sending range. \n
			:param class_py: WIDE | MEDium | LOCal WIDE Wide Area MEDium Medium Range LOCal Local Area
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_scalar_to_str(class_py, enums.RangeClass)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:CLASs {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.RangeClass:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:CLASs \n
		Snippet: value: enums.RangeClass = driver.sense.espectrum.msr.classPy.get(subBlock = repcap.SubBlock.Default) \n
		Defines the class of the base station according to its sending range. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: class_py: WIDE | MEDium | LOCal WIDE Wide Area MEDium Medium Range LOCal Local Area"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:CLASs?')
		return Conversions.str_to_scalar_enum(response, enums.RangeClass)
