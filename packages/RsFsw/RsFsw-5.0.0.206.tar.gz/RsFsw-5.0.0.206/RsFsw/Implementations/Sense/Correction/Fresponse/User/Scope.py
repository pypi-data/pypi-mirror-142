from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scope:
	"""Scope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scope", core, parent)

	def set(self, frames: enums.FramesScope) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SCOPe \n
		Snippet: driver.sense.correction.fresponse.user.scope.set(frames = enums.FramesScope.ALL) \n
		Determines whether the frequency response correction settings are applied to all active measurement channels, or only the
		currently selected channel. \n
			:param frames: CHANnel | ALL CHANnel The frequency response correction settings are applied to the currently selected channel only. To select a channel, use method RsFsw.Instrument.Select.set. For a list of available channels, use method RsFsw.Instrument.ListPy.get_. ALL The frequency response correction settings are applied to all active measurement channels.
		"""
		param = Conversions.enum_scalar_to_str(frames, enums.FramesScope)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:SCOPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FramesScope:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:SCOPe \n
		Snippet: value: enums.FramesScope = driver.sense.correction.fresponse.user.scope.get() \n
		Determines whether the frequency response correction settings are applied to all active measurement channels, or only the
		currently selected channel. \n
			:return: frames: CHANnel | ALL CHANnel The frequency response correction settings are applied to the currently selected channel only. To select a channel, use method RsFsw.Instrument.Select.set. For a list of available channels, use method RsFsw.Instrument.ListPy.get_. ALL The frequency response correction settings are applied to all active measurement channels."""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:SCOPe?')
		return Conversions.str_to_scalar_enum(response, enums.FramesScope)
