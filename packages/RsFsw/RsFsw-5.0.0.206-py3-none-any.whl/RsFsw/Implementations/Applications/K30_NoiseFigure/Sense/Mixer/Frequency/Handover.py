from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("handover", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:MIXer:FREQuency:HANDover \n
		Snippet: driver.applications.k30NoiseFigure.sense.mixer.frequency.handover.set(frequency = 1.0) \n
		This command defines the frequency at which the mixer switches from one range to the next (if two different ranges are
		selected) . The handover frequency for each band can be selected freely within the overlapping frequency range.
		This command is only available if the external mixer is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:MIXer:FREQuency:HANDover {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:FREQuency:HANDover \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.mixer.frequency.handover.get() \n
		This command defines the frequency at which the mixer switches from one range to the next (if two different ranges are
		selected) . The handover frequency for each band can be selected freely within the overlapping frequency range.
		This command is only available if the external mixer is active (see [SENSe:]MIXer<x>[:STATe]) . \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:MIXer:FREQuency:HANDover?')
		return Conversions.str_to_float(response)
