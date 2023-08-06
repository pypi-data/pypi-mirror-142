from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INITiate:CONTinuous \n
		Snippet: driver.initiate.continuous.set(state = False) \n
		This command controls the measurement mode for an individual channel. Note that in single measurement mode, you can
		synchronize to the end of the measurement with *OPC, *OPC? or *WAI. In continuous measurement mode, synchronization to
		the end of the measurement is not possible. Thus, it is not recommended that you use continuous measurement mode in
		remote control, as results like trace data or markers are only valid after a single measurement end synchronization. For
		details on synchronization see Remote control via SCPI. If the measurement mode is changed for a channel while the
		Sequencer is active (see method RsFsw.Initiate.Sequencer.Immediate.set) the mode is only considered the next time the
		measurement in that channel is activated by the Sequencer. \n
			:param state: ON | OFF | 0 | 1 ON | 1 Continuous measurement OFF | 0 Single measurement
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INITiate:CONTinuous {param}')
