from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MlCalc:
	"""MlCalc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mlCalc", core, parent)

	def set(self, function: enums.FunctionB, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:MLCalc \n
		Snippet: driver.sense.espectrum.range.mlCalc.set(function = enums.FunctionB.MAX, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Defines the function used to calculate the limit line for the n-th power class for overlapping ranges in Multi-SEM
		measurements. For details see 'Limit calculation for individual ranges'. \n
			:param function: NONE | MAX | SUM NONE (reference ranges only:) the limit of the reference range is used; Reference ranges always use the function 'NONE'. SUM sum of the two limit lines (calculated for linear powers) is used MAX maximum of the two limit lines is used
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(function, enums.FunctionB)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:MLCalc {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> enums.FunctionB:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:MLCalc \n
		Snippet: value: enums.FunctionB = driver.sense.espectrum.range.mlCalc.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Defines the function used to calculate the limit line for the n-th power class for overlapping ranges in Multi-SEM
		measurements. For details see 'Limit calculation for individual ranges'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: function: NONE | MAX | SUM NONE (reference ranges only:) the limit of the reference range is used; Reference ranges always use the function 'NONE'. SUM sum of the two limit lines (calculated for linear powers) is used MAX maximum of the two limit lines is used"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:MLCalc?')
		return Conversions.str_to_scalar_enum(response, enums.FunctionB)
