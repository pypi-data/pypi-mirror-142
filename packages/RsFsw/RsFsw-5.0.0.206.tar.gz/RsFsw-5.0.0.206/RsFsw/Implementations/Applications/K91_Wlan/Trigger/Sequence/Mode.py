from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, source: enums.TriggerSourceH) -> None:
		"""SCPI: TRIGger[:SEQuence]:MODE \n
		Snippet: driver.applications.k91Wlan.trigger.sequence.mode.set(source = enums.TriggerSourceH.AF) \n
		Defines the trigger source. Note that this command is maintained for compatibility reasons only. Use the method RsFsw.
		Applications.K17_Mcgd.Trigger.Sequence.Source.set commands for new remote control programs. This command configures how
		triggering is to be performed. \n
			:param source: MANual | IMMediate | EXTernal | VIDeo | RFPower | IFPower | TV | AF | AM | FM | PM | AMRelative | LXI | TIME | SLEFt | SRIGht | SMPX | SMONo | SSTereo | SRDS | SPILot | BBPower | MASK | PSENsor | TDTRigger | IQPower | EXT2 | EXT3 | TUNit
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceH)
		self._core.io.write(f'TRIGger:SEQuence:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerSourceH:
		"""SCPI: TRIGger[:SEQuence]:MODE \n
		Snippet: value: enums.TriggerSourceH = driver.applications.k91Wlan.trigger.sequence.mode.get() \n
		Defines the trigger source. Note that this command is maintained for compatibility reasons only. Use the method RsFsw.
		Applications.K17_Mcgd.Trigger.Sequence.Source.set commands for new remote control programs. This command configures how
		triggering is to be performed. \n
			:return: source: MANual | IMMediate | EXTernal | VIDeo | RFPower | IFPower | TV | AF | AM | FM | PM | AMRelative | LXI | TIME | SLEFt | SRIGht | SMPX | SMONo | SSTereo | SRDS | SPILot | BBPower | MASK | PSENsor | TDTRigger | IQPower | EXT2 | EXT3 | TUNit"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceH)
