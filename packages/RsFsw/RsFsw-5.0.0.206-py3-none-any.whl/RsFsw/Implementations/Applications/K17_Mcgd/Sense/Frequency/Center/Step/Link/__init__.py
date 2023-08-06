from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	@property
	def factor(self):
		"""factor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_factor'):
			from .Factor import Factor
			self._factor = Factor(self._core, self._cmd_group)
		return self._factor

	def set(self, step_link: enums.FrequencyCouplingLinkB) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK \n
		Snippet: driver.applications.k17Mcgd.sense.frequency.center.step.link.set(step_link = enums.FrequencyCouplingLinkB.OFF) \n
		This command couples and decouples the center frequency step size to the span or the resolution bandwidth. \n
			:param step_link: SPAN | RBW | OFF SPAN Couples the step size to the span. Available for measurements in the frequency domain. OFF Decouples the step size.
		"""
		param = Conversions.enum_scalar_to_str(step_link, enums.FrequencyCouplingLinkB)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP:LINK {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FrequencyCouplingLinkB:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP:LINK \n
		Snippet: value: enums.FrequencyCouplingLinkB = driver.applications.k17Mcgd.sense.frequency.center.step.link.get() \n
		This command couples and decouples the center frequency step size to the span or the resolution bandwidth. \n
			:return: step_link: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP:LINK?')
		return Conversions.str_to_scalar_enum(response, enums.FrequencyCouplingLinkB)

	def clone(self) -> 'Link':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Link(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
