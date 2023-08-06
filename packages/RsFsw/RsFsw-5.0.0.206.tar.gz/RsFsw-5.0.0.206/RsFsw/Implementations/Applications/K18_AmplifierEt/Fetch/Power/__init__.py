from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 43 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def cfactor(self):
		"""cfactor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def gain(self):
		"""gain commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def inputPy(self):
		"""inputPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def sensor(self):
		"""sensor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sensor'):
			from .Sensor import Sensor
			self._sensor = Sensor(self._core, self._cmd_group)
		return self._sensor

	@property
	def output(self):
		"""output commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def p1Db(self):
		"""p1Db commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_p1Db'):
			from .P1Db import P1Db
			self._p1Db = P1Db(self._core, self._cmd_group)
		return self._p1Db

	@property
	def p2Db(self):
		"""p2Db commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_p2Db'):
			from .P2Db import P2Db
			self._p2Db = P2Db(self._core, self._cmd_group)
		return self._p2Db

	@property
	def p3Db(self):
		"""p3Db commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_p3Db'):
			from .P3Db import P3Db
			self._p3Db = P3Db(self._core, self._cmd_group)
		return self._p3Db

	@property
	def obw(self):
		"""obw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .Obw import Obw
			self._obw = Obw(self._core, self._cmd_group)
		return self._obw

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
