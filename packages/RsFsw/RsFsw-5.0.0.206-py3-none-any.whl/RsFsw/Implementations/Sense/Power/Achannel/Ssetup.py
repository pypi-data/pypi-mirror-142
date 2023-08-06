from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssetup:
	"""Ssetup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssetup", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SSETup \n
		Snippet: driver.sense.power.achannel.ssetup.set(state = False) \n
		This command defines whether adjacent channels are defined symmetrically or not. For more information see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param state: ON | OFF | 1 | 0 ON | 1 The upper and lower adjacent and alternate channels are defined symmetrically. This is the default behaviour and corresponds to the behavior in firmware versions before 2.10. OFF | 0 The upper and lower channels can be configured differently.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:SSETup {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:SSETup \n
		Snippet: value: bool = driver.sense.power.achannel.ssetup.get() \n
		This command defines whether adjacent channels are defined symmetrically or not. For more information see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 The upper and lower adjacent and alternate channels are defined symmetrically. This is the default behaviour and corresponds to the behavior in firmware versions before 2.10. OFF | 0 The upper and lower channels can be configured differently."""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SSETup?')
		return Conversions.str_to_bool(response)
