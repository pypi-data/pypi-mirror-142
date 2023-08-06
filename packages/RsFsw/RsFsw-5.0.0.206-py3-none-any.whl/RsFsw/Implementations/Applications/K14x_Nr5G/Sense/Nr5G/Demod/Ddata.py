from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddata:
	"""Ddata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddata", core, parent)

	def set(self, state: enums.DemodDataSelect) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:DDATa \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.ddata.set(state = enums.DemodDataSelect.ADEScramble) \n
		This command selects the point at which the data is demodulated for the bitstream. \n
			:param state: ADEScramble Demodulates the descrambled data. BDEScramble Demodulates the scrambled data. DPData Demodulates the decoded data.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.DemodDataSelect)
		self._core.io.write(f'SENSe:NR5G:DEMod:DDATa {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DemodDataSelect:
		"""SCPI: [SENSe]:NR5G:DEMod:DDATa \n
		Snippet: value: enums.DemodDataSelect = driver.applications.k14Xnr5G.sense.nr5G.demod.ddata.get() \n
		This command selects the point at which the data is demodulated for the bitstream. \n
			:return: state: ADEScramble Demodulates the descrambled data. BDEScramble Demodulates the scrambled data. DPData Demodulates the decoded data."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:DDATa?')
		return Conversions.str_to_scalar_enum(response, enums.DemodDataSelect)
