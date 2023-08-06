from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Egate:
	"""Egate commands group definition. 13 total commands, 8 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("egate", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def level(self):
		"""level commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def polarity(self):
		"""polarity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_polarity'):
			from .Polarity import Polarity
			self._polarity = Polarity(self._core, self._cmd_group)
		return self._polarity

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def holdoff(self):
		"""holdoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import Holdoff
			self._holdoff = Holdoff(self._core, self._cmd_group)
		return self._holdoff

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def continuous(self):
		"""continuous commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_continuous'):
			from .Continuous import Continuous
			self._continuous = Continuous(self._core, self._cmd_group)
		return self._continuous

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.set(state = False) \n
		This command turns gated measurements on and off. For measurements with an external trigger gate, the measured values are
		recorded as long as the gate is opened. During a sweep the gate can be opened and closed several times.
		The synchronization mechanisms with *OPC, *OPC? and *WAI remain completely unaffected. See '(Measurement) Points'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:EGATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:EGATe \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.sweep.egate.get() \n
		This command turns gated measurements on and off. For measurements with an external trigger gate, the measured values are
		recorded as long as the gate is opened. During a sweep the gate can be opened and closed several times.
		The synchronization mechanisms with *OPC, *OPC? and *WAI remain completely unaffected. See '(Measurement) Points'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Egate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Egate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
