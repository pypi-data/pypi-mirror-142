from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, segment: float) -> None:
		"""SCPI: [SENSe]:NR5G:SEGMent:SELect \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.segment.select.set(segment = 1.0) \n
		This command selects the analyzed segment for a segmented capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:param segment: numeric value (integer only) The value range depends on the number of captured segments ([SENSe:]SWEep:SCAPture:EVENts) .
		"""
		param = Conversions.decimal_value_to_str(segment)
		self._core.io.write(f'SENSe:NR5G:SEGMent:SELect {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NR5G:SEGMent:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.segment.select.get() \n
		This command selects the analyzed segment for a segmented capture.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on segmented capture ([SENSe:]SWEep:SCAPture:STATe) . \n
			:return: segment: numeric value (integer only) The value range depends on the number of captured segments ([SENSe:]SWEep:SCAPture:EVENts) ."""
		response = self._core.io.query_str(f'SENSe:NR5G:SEGMent:SELect?')
		return Conversions.str_to_float(response)
