from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, attenuation: float) -> None:
		"""SCPI: INPut:ATTenuation \n
		Snippet: driver.applications.k14Xnr5G.inputPy.attenuation.set(attenuation = 1.0) \n
		This command defines the RF attenuation level.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Decouple attenuation from reference level (method RsFsw.Applications.K10x_Lte.InputPy.Attenuation.Auto.set) . \n
			:param attenuation: Unit: dB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'INPut:ATTenuation {param}')

	def get(self) -> float:
		"""SCPI: INPut:ATTenuation \n
		Snippet: value: float = driver.applications.k14Xnr5G.inputPy.attenuation.get() \n
		This command defines the RF attenuation level.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Decouple attenuation from reference level (method RsFsw.Applications.K10x_Lte.InputPy.Attenuation.Auto.set) . \n
			:return: attenuation: Unit: dB"""
		response = self._core.io.query_str(f'INPut:ATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
