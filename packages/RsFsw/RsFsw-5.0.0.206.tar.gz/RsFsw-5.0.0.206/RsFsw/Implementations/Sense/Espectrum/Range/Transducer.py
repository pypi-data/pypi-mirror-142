from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transducer:
	"""Transducer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transducer", core, parent)

	def set(self, transducer: str, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:TRANsducer \n
		Snippet: driver.sense.espectrum.range.transducer.set(transducer = '1', subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		This command selects a transducer factor for a SEM range. Note that
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- the transducer must cover at least the span of the range
			- the x-axis has to be linear
			- the unit has to be dB \n
			:param transducer: String containing the transducer file name, including the path information.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.value_to_quoted_str(transducer)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:TRANsducer {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> str:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:TRANsducer \n
		Snippet: value: str = driver.sense.espectrum.range.transducer.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		This command selects a transducer factor for a SEM range. Note that
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- the transducer must cover at least the span of the range
			- the x-axis has to be linear
			- the unit has to be dB \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: transducer: String containing the transducer file name, including the path information."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:TRANsducer?')
		return trim_str_response(response)
