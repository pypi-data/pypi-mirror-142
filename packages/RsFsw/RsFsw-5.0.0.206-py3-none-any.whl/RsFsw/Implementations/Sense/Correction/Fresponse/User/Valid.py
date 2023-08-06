from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Valid:
	"""Valid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("valid", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:VALid \n
		Snippet: value: float = driver.sense.correction.fresponse.user.valid.get() \n
		This command queries the validity of the user-defined correction settings. \n
			:return: validity: 0 | 1 1 The setting is valid. 0 The setting is not valid."""
		response = self._core.io.query_str(f'SENSe:CORRection:FRESponse:USER:VALid?')
		return Conversions.str_to_float(response)
