from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlpMode:
	"""AlpMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpMode", core, parent)

	def set(self, mode: enums.AcpLimitEvalMode) -> None:
		"""SCPI: [SENSe]:NR5G:ACPower:ALPMode \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.acPower.alpMode.set(mode = enums.AcpLimitEvalMode.ABSolute) \n
		This command selects the limit evaluation mode for ACLR measurements in combined measurement mode. \n
			:param mode: ABSolute Checks against the absolute limits. RELative Checks against the relative limits. OR Checks against both absolute and relative limits according to 3GPP.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AcpLimitEvalMode)
		self._core.io.write(f'SENSe:NR5G:ACPower:ALPMode {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AcpLimitEvalMode:
		"""SCPI: [SENSe]:NR5G:ACPower:ALPMode \n
		Snippet: value: enums.AcpLimitEvalMode = driver.applications.k14Xnr5G.sense.nr5G.acPower.alpMode.get() \n
		This command selects the limit evaluation mode for ACLR measurements in combined measurement mode. \n
			:return: mode: ABSolute Checks against the absolute limits. RELative Checks against the relative limits. OR Checks against both absolute and relative limits according to 3GPP."""
		response = self._core.io.query_str(f'SENSe:NR5G:ACPower:ALPMode?')
		return Conversions.str_to_scalar_enum(response, enums.AcpLimitEvalMode)
