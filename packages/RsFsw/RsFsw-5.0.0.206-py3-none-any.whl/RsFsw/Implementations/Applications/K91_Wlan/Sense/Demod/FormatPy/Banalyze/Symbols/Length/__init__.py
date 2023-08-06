from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, num_data_symbols: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:LENGth \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.length.set(num_data_symbols = 1.0) \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe command
		is set to false, this command specifies the number of PPDU data symbols after the Analysis Interval Offset (see
		[SENSe:]DEMod:FORMat:BANalyze:SYMBols:OFFSet) which are to be analyzed.
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe command is set to true, then this command has no effect. \n
			:param num_data_symbols: Range: 0 to 10000
		"""
		param = Conversions.decimal_value_to_str(num_data_symbols)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:LENGth \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.length.get() \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe command
		is set to false, this command specifies the number of PPDU data symbols after the Analysis Interval Offset (see
		[SENSe:]DEMod:FORMat:BANalyze:SYMBols:OFFSet) which are to be analyzed.
		If the [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe command is set to true, then this command has no effect. \n
			:return: num_data_symbols: Range: 0 to 10000"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:LENGth?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Length':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Length(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
