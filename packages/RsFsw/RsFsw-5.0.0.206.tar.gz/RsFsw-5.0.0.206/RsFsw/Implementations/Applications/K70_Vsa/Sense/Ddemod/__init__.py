from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddemod:
	"""Ddemod commands group definition. 138 total commands, 31 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddemod", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def pattern(self):
		"""pattern commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def prate(self):
		"""prate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prate'):
			from .Prate import Prate
			self._prate = Prate(self._core, self._cmd_group)
		return self._prate

	@property
	def optimization(self):
		"""optimization commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimization'):
			from .Optimization import Optimization
			self._optimization = Optimization(self._core, self._cmd_group)
		return self._optimization

	@property
	def sband(self):
		"""sband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sband'):
			from .Sband import Sband
			self._sband = Sband(self._core, self._cmd_group)
		return self._sband

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def ecalc(self):
		"""ecalc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ecalc'):
			from .Ecalc import Ecalc
			self._ecalc = Ecalc(self._core, self._cmd_group)
		return self._ecalc

	@property
	def equalizer(self):
		"""equalizer commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_equalizer'):
			from .Equalizer import Equalizer
			self._equalizer = Equalizer(self._core, self._cmd_group)
		return self._equalizer

	@property
	def epRate(self):
		"""epRate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_epRate'):
			from .EpRate import EpRate
			self._epRate = EpRate(self._core, self._cmd_group)
		return self._epRate

	@property
	def normalize(self):
		"""normalize commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_normalize'):
			from .Normalize import Normalize
			self._normalize = Normalize(self._core, self._cmd_group)
		return self._normalize

	@property
	def fsk(self):
		"""fsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	@property
	def ask(self):
		"""ask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ask'):
			from .Ask import Ask
			self._ask = Ask(self._core, self._cmd_group)
		return self._ask

	@property
	def apsk(self):
		"""apsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apsk'):
			from .Apsk import Apsk
			self._apsk = Apsk(self._core, self._cmd_group)
		return self._apsk

	@property
	def fsync(self):
		"""fsync commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsync'):
			from .Fsync import Fsync
			self._fsync = Fsync(self._core, self._cmd_group)
		return self._fsync

	@property
	def kdata(self):
		"""kdata commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_kdata'):
			from .Kdata import Kdata
			self._kdata = Kdata(self._core, self._cmd_group)
		return self._kdata

	@property
	def msk(self):
		"""msk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msk'):
			from .Msk import Msk
			self._msk = Msk(self._core, self._cmd_group)
		return self._msk

	@property
	def psk(self):
		"""psk commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psk'):
			from .Psk import Psk
			self._psk = Psk(self._core, self._cmd_group)
		return self._psk

	@property
	def signal(self):
		"""signal commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import Signal
			self._signal = Signal(self._core, self._cmd_group)
		return self._signal

	@property
	def qam(self):
		"""qam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Qam import Qam
			self._qam = Qam(self._core, self._cmd_group)
		return self._qam

	@property
	def qpsk(self):
		"""qpsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qpsk'):
			from .Qpsk import Qpsk
			self._qpsk = Qpsk(self._core, self._cmd_group)
		return self._qpsk

	@property
	def rlength(self):
		"""rlength commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import Rlength
			self._rlength = Rlength(self._core, self._cmd_group)
		return self._rlength

	@property
	def search(self):
		"""search commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_search'):
			from .Search import Search
			self._search = Search(self._core, self._cmd_group)
		return self._search

	@property
	def standard(self):
		"""standard commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	@property
	def factory(self):
		"""factory commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_factory'):
			from .Factory import Factory
			self._factory = Factory(self._core, self._cmd_group)
		return self._factory

	@property
	def filterPy(self):
		"""filterPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def mfilter(self):
		"""mfilter commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfilter'):
			from .Mfilter import Mfilter
			self._mfilter = Mfilter(self._core, self._cmd_group)
		return self._mfilter

	@property
	def tfilter(self):
		"""tfilter commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_tfilter'):
			from .Tfilter import Tfilter
			self._tfilter = Tfilter(self._core, self._cmd_group)
		return self._tfilter

	@property
	def mapping(self):
		"""mapping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import Mapping
			self._mapping = Mapping(self._core, self._cmd_group)
		return self._mapping

	@property
	def preset(self):
		"""preset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def user(self):
		"""user commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Ddemod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ddemod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
