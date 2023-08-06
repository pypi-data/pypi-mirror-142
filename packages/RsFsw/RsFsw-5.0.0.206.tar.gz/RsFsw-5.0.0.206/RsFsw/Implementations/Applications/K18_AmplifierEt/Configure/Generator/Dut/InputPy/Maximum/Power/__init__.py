from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:DUT:INPut:MAXimum:POWer \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.dut.inputPy.maximum.power.set(level = 1.0) \n
		This command defines the maximum generator output power. \n
			:param level: Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:DUT:INPut:MAXimum:POWer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:DUT:INPut:MAXimum:POWer \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.dut.inputPy.maximum.power.get() \n
		This command defines the maximum generator output power. \n
			:return: level: Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:GENerator:DUT:INPut:MAXimum:POWer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
