from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def auto(self):
		"""auto commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def protection(self):
		"""protection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	def set(self, attenuation: float) -> None:
		"""SCPI: INPut:ATTenuation \n
		Snippet: driver.inputPy.attenuation.set(attenuation = 1.0) \n
		This command defines the total attenuation for RF input. If an electronic attenuator is available and active, the command
		defines a mechanical attenuation (see method RsFsw.Applications.K18_AmplifierEt.InputPy.Eatt.State.set) . If you set the
		attenuation manually, it is no longer coupled to the reference level, but the reference level is coupled to the
		attenuation. Thus, if the current reference level is not compatible with an attenuation that has been set manually, the
		command also adjusts the reference level. This function is not available if the optional Digital Baseband Interface is
		active. \n
			:param attenuation: Range: see data sheet , Unit: DB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'INPut:ATTenuation {param}')

	def get(self) -> float:
		"""SCPI: INPut:ATTenuation \n
		Snippet: value: float = driver.inputPy.attenuation.get() \n
		This command defines the total attenuation for RF input. If an electronic attenuator is available and active, the command
		defines a mechanical attenuation (see method RsFsw.Applications.K18_AmplifierEt.InputPy.Eatt.State.set) . If you set the
		attenuation manually, it is no longer coupled to the reference level, but the reference level is coupled to the
		attenuation. Thus, if the current reference level is not compatible with an attenuation that has been set manually, the
		command also adjusts the reference level. This function is not available if the optional Digital Baseband Interface is
		active. \n
			:return: attenuation: Range: see data sheet , Unit: DB"""
		response = self._core.io.query_str(f'INPut:ATTenuation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
