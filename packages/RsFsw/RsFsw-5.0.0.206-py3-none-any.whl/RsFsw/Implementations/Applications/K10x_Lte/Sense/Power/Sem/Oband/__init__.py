from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oband:
	"""Oband commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oband", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, operating_band: float) -> None:
		"""SCPI: [SENSe]:POWer:SEM:OBANd \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.oband.set(operating_band = 1.0) \n
		This command selects the SEM for a specific operating band.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on selection of operating band related SEM limits ([SENSe:]POWer:SEM:OBANd:STATe) . \n
			:param operating_band: numeric value (integer only)
		"""
		param = Conversions.decimal_value_to_str(operating_band)
		self._core.io.write(f'SENSe:POWer:SEM:OBANd {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:SEM:OBANd \n
		Snippet: value: float = driver.applications.k10Xlte.sense.power.sem.oband.get() \n
		This command selects the SEM for a specific operating band.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on selection of operating band related SEM limits ([SENSe:]POWer:SEM:OBANd:STATe) . \n
			:return: operating_band: numeric value (integer only)"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:OBANd?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Oband':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oband(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
