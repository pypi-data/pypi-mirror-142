from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqcThreshold:
	"""IqcThreshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqcThreshold", core, parent)

	def set(self, correlation_lev: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:IQCThreshold \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.iqcThreshold.set(correlation_lev = 1.0) \n
		This command sets the I/Q correlation threshold for pattern matching in percent. A high level means stricter matching. \n
			:param correlation_lev: Range: 10.0 to 100.0, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(correlation_lev)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:IQCThreshold {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:IQCThreshold \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.sync.iqcThreshold.get() \n
		This command sets the I/Q correlation threshold for pattern matching in percent. A high level means stricter matching. \n
			:return: correlation_lev: Range: 10.0 to 100.0, Unit: PCT"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:IQCThreshold?')
		return Conversions.str_to_float(response)
