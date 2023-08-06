from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("handover", core, parent)

	def set(self, arg_0: float) -> None:
		"""SCPI: [SENSe]:MIXer:FREQuency:HANDover \n
		Snippet: driver.applications.k40PhaseNoise.sense.mixer.frequency.handover.set(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'SENSe:MIXer:FREQuency:HANDover {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:FREQuency:HANDover \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.mixer.frequency.handover.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:FREQuency:HANDover?')
		return Conversions.str_to_float(response)
