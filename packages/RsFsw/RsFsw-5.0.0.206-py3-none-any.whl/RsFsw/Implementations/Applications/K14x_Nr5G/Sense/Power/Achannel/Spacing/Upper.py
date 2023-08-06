from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, spacing: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:UPPer \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.spacing.upper.set(spacing = 1.0) \n
		No command help available \n
			:param spacing: No help available
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:UPPer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:UPPer \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.spacing.upper.get() \n
		No command help available \n
			:return: spacing: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:UPPer?')
		return Conversions.str_to_float(response)
