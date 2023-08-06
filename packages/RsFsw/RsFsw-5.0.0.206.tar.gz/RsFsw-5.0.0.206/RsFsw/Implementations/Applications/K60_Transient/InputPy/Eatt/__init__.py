from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eatt:
	"""Eatt commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eatt", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, attenuation: float) -> None:
		"""SCPI: INPut:EATT \n
		Snippet: driver.applications.k60Transient.inputPy.eatt.set(attenuation = 1.0) \n
		This command defines an electronic attenuation manually. Automatic mode must be switched off (INP:EATT:AUTO OFF, see
		method RsFsw.Applications.K18_AmplifierEt.InputPy.Eatt.Auto.set) . If the current reference level is not compatible with
		an attenuation that has been set manually, the command also adjusts the reference level. \n
			:param attenuation: attenuation in dB Range: see data sheet , Unit: DB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'INPut:EATT {param}')

	def get(self) -> float:
		"""SCPI: INPut:EATT \n
		Snippet: value: float = driver.applications.k60Transient.inputPy.eatt.get() \n
		This command defines an electronic attenuation manually. Automatic mode must be switched off (INP:EATT:AUTO OFF, see
		method RsFsw.Applications.K18_AmplifierEt.InputPy.Eatt.Auto.set) . If the current reference level is not compatible with
		an attenuation that has been set manually, the command also adjusts the reference level. \n
			:return: attenuation: attenuation in dB Range: see data sheet , Unit: DB"""
		response = self._core.io.query_str(f'INPut:EATT?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Eatt':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eatt(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
