from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spot:
	"""Spot commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spot", core, parent)

	@property
	def hot(self):
		"""hot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hot'):
			from .Hot import Hot
			self._hot = Hot(self._core, self._cmd_group)
		return self._hot

	@property
	def cold(self):
		"""cold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cold'):
			from .Cold import Cold
			self._cold = Cold(self._core, self._cmd_group)
		return self._cold

	def set(self, enr: float) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SPOT \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.spot.set(enr = 1.0) \n
		This command defines the constant ENR for all measurement points during the actual measurement. \n
			:param enr: Unit: DB
		"""
		param = Conversions.decimal_value_to_str(enr)
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:SPOT {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SPOT \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.spot.get() \n
		This command defines the constant ENR for all measurement points during the actual measurement. \n
			:return: enr: Unit: DB"""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:MEASurement:SPOT?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Spot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
