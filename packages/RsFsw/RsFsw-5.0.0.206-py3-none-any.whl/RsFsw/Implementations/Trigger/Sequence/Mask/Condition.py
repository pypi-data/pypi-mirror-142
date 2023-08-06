from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Condition:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def set(self, condition: enums.MaskCondition) -> None:
		"""SCPI: TRIGger[:SEQuence]:MASK:CONDition \n
		Snippet: driver.trigger.sequence.mask.condition.set(condition = enums.MaskCondition.ENTer) \n
		This command sets the condition that activates the frequency mask trigger. For details see 'Triggering on specific
		frequency events (frequency mask trigger) '. \n
			:param condition: ENTer Triggers on entering the frequency mask. LEAVing Triggers on leaving the frequency mask.
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.MaskCondition)
		self._core.io.write(f'TRIGger:SEQuence:MASK:CONDition {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.MaskCondition:
		"""SCPI: TRIGger[:SEQuence]:MASK:CONDition \n
		Snippet: value: enums.MaskCondition = driver.trigger.sequence.mask.condition.get() \n
		This command sets the condition that activates the frequency mask trigger. For details see 'Triggering on specific
		frequency events (frequency mask trigger) '. \n
			:return: condition: ENTer Triggers on entering the frequency mask. LEAVing Triggers on leaving the frequency mask."""
		response = self._core.io.query_str(f'TRIGger:SEQuence:MASK:CONDition?')
		return Conversions.str_to_scalar_enum(response, enums.MaskCondition)
