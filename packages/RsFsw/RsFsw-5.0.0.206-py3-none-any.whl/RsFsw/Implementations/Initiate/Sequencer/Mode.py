from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.SequencerMode) -> None:
		"""SCPI: INITiate:SEQuencer:MODE \n
		Snippet: driver.initiate.sequencer.mode.set(mode = enums.SequencerMode.CDEFined) \n
		Defines the capture mode for the entire measurement sequence and all measurement groups and channels it contains. Note:
		In order to synchronize to the end of a measurement sequence using *OPC, *OPC? or *WAI you must use SINGle Sequence mode. \n
			:param mode: SINGle Each measurement group is started one after the other in the order of definition. All measurement channels in a group are started simultaneously and performed once. After all measurements are completed, the next group is started. After the last group, the measurement sequence is finished. CONTinuous Each measurement group is started one after the other in the order of definition. All measurement channels in a group are started simultaneously and performed once. After all measurements are completed, the next group is started. After the last group, the measurement sequence restarts with the first one and continues until it is stopped explicitely.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SequencerMode)
		self._core.io.write(f'INITiate:SEQuencer:MODE {param}')
