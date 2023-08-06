from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INITiate:CONTinuous \n
		Snippet: driver.applications.k10Xlte.initiate.continuous.set(state = False) \n
		This command controls the measurement mode for an individual channel. Note that in single measurement mode, you can
		synchronize to the end of the measurement with *OPC, *OPC? or *WAI. In continuous measurement mode, synchronization to
		the end of the measurement is not possible. Thus, it is not recommended that you use continuous measurement mode in
		remote control, as results like trace data or markers are only valid after a single measurement end synchronization. For
		details on synchronization see Remote control via SCPI. \n
			:param state: ON | OFF | 0 | 1 ON | 1 Continuous measurement OFF | 0 Single measurement
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INITiate:CONTinuous {param}')

	def get(self) -> bool:
		"""SCPI: INITiate:CONTinuous \n
		Snippet: value: bool = driver.applications.k10Xlte.initiate.continuous.get() \n
		This command controls the measurement mode for an individual channel. Note that in single measurement mode, you can
		synchronize to the end of the measurement with *OPC, *OPC? or *WAI. In continuous measurement mode, synchronization to
		the end of the measurement is not possible. Thus, it is not recommended that you use continuous measurement mode in
		remote control, as results like trace data or markers are only valid after a single measurement end synchronization. For
		details on synchronization see Remote control via SCPI. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 Continuous measurement OFF | 0 Single measurement"""
		response = self._core.io.query_str(f'INITiate:CONTinuous?')
		return Conversions.str_to_bool(response)
