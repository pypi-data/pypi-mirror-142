from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	def set(self, source: enums.SourceSequence) -> None:
		"""SCPI: TRIGger:TSHelper:SEQuence \n
		Snippet: driver.applications.k14Xnr5G.trigger.tsHelper.sequence.set(source = enums.SourceSequence.CLOop) \n
		This command select the type of measurement sequence for combined measurement. \n
			:param source: The selected sequence has an impact on the trigger settings. If you select a certain sequence and change, for example, the trigger source or trigger input / output configuration, the sequence type automatically returns to manual. CLOop Closed-loop sequence. MANual Custom trigger configuration. OLOop Open-loop sequence. PERiodic Periodic sequence.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceSequence)
		self._core.io.write(f'TRIGger:TSHelper:SEQuence {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SourceSequence:
		"""SCPI: TRIGger:TSHelper:SEQuence \n
		Snippet: value: enums.SourceSequence = driver.applications.k14Xnr5G.trigger.tsHelper.sequence.get() \n
		This command select the type of measurement sequence for combined measurement. \n
			:return: source: The selected sequence has an impact on the trigger settings. If you select a certain sequence and change, for example, the trigger source or trigger input / output configuration, the sequence type automatically returns to manual. CLOop Closed-loop sequence. MANual Custom trigger configuration. OLOop Open-loop sequence. PERiodic Periodic sequence."""
		response = self._core.io.query_str(f'TRIGger:TSHelper:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.SourceSequence)
