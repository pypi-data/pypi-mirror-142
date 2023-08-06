from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Width:
	"""Width commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("width", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: RIQ:PFM:WIDTh \n
		Snippet: driver.applications.k6Pulse.riq.pfm.width.set(time = 1.0) \n
		Sets/queries the pulse width for polynomial FM type reference I/Q data. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'RIQ:PFM:WIDTh {param}')

	def get(self) -> float:
		"""SCPI: RIQ:PFM:WIDTh \n
		Snippet: value: float = driver.applications.k6Pulse.riq.pfm.width.get() \n
		Sets/queries the pulse width for polynomial FM type reference I/Q data. \n
			:return: time: Unit: S"""
		response = self._core.io.query_str(f'RIQ:PFM:WIDTh?')
		return Conversions.str_to_float(response)
