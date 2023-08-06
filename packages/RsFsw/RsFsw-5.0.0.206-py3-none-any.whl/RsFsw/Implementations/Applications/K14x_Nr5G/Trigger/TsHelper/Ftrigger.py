from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ftrigger:
	"""Ftrigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ftrigger", core, parent)

	def set(self, source: enums.FrameTriggerSource) -> None:
		"""SCPI: TRIGger:TSHelper:FTRigger \n
		Snippet: driver.applications.k14Xnr5G.trigger.tsHelper.ftrigger.set(source = enums.FrameTriggerSource.AVAilable) \n
		This command select the availability of a frame trigger in a combined measurement sequence. \n
			:param source: AVAilable Frame trigger available (external trigger) . NAVailable Time trigger available. RSLots No trigger available.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.FrameTriggerSource)
		self._core.io.write(f'TRIGger:TSHelper:FTRigger {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrameTriggerSource:
		"""SCPI: TRIGger:TSHelper:FTRigger \n
		Snippet: value: enums.FrameTriggerSource = driver.applications.k14Xnr5G.trigger.tsHelper.ftrigger.get() \n
		This command select the availability of a frame trigger in a combined measurement sequence. \n
			:return: source: AVAilable Frame trigger available (external trigger) . NAVailable Time trigger available. RSLots No trigger available."""
		response = self._core.io.query_str(f'TRIGger:TSHelper:FTRigger?')
		return Conversions.str_to_scalar_enum(response, enums.FrameTriggerSource)
