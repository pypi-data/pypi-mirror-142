from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:IQAVg:COUNt:CURRent \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.sweep.iqAvg.count.current.get() \n
		Only available for backward compatibility. Queries the current measurement out of a sequence of measurements that
		averages I/Q data. \n
			:return: measurement: numeric value"""
		response = self._core.io.query_str(f'SENSe:SWEep:IQAVg:COUNt:CURRent?')
		return Conversions.str_to_float(response)
