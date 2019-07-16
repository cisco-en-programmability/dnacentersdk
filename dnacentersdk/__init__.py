# -*- coding: utf-8 -*-
"""Community-developed Python SDK for the DNA Center APIs.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import logging

from ._metadata import *
from ._version import get_versions
from .api import DNACenterAPI
from .exceptions import (
    AccessTokenError, ApiError,
    RateLimitError, MalformedRequest,
    RateLimitWarning, dnacentersdkException,
)
from .models.mydict import mydict_data_factory

from .models.schema_validator import (
    JSONSchemaValidator01B09A254B9AB259,
    JSONSchemaValidator00AeC9B1422AB27E,
    JSONSchemaValidator7781Fa0548A98342,
    JSONSchemaValidator109D1B4F4289Aecd,
    JSONSchemaValidator6099Da82477B858A,
    JSONSchemaValidator83A3B9404Cb88787,
    JSONSchemaValidator9480Fa1F47Ca9254,
    JSONSchemaValidator9C9A785741CbB41F,
    JSONSchemaValidatorA7B42836408A8E74,
    JSONSchemaValidator62B05B2C40A9B216,
    JSONSchemaValidatorF393Abe84989Bb48,
    JSONSchemaValidatorD0A1Abfa435B841D,
    JSONSchemaValidatorF6B119Ad4D4AAf16,
    JSONSchemaValidatorC8Bf6B65414A9Bc7,
    JSONSchemaValidator00A2Fa6146089317,
    JSONSchemaValidator2E9DB85840FbB1Cf,
    JSONSchemaValidator1399891C42A8Be64,
    JSONSchemaValidator4695090D403B8Eaa,
    JSONSchemaValidator45Bc7A8344A8Bc1E,
    JSONSchemaValidator4D86A993469A9Da9,
    JSONSchemaValidator8091A9B84BfbA53B,
    JSONSchemaValidator429C28154BdaA13D,
    JSONSchemaValidatorCaa3Ea704D78B37E,
    JSONSchemaValidatorEab7Abe048Fb99Ad,
    JSONSchemaValidatorC1A359B14C89B573,
    JSONSchemaValidatorEe9AAb01487A8896,
    JSONSchemaValidator069D9823451B892D,
    JSONSchemaValidator17929Bc7465BB564,
    JSONSchemaValidator10B06A6A4F7BB3Cb,
    JSONSchemaValidator1Da5Ebdd434AAcfe,
    JSONSchemaValidator44974Ba5435A801D,
    JSONSchemaValidator4C8CAb5F435A80F4,
    JSONSchemaValidator55B439Dc4239B140,
    JSONSchemaValidator6BacB8D14639Bdc7,
    JSONSchemaValidator4D9CA8E2431A8A24,
    JSONSchemaValidator3D9B99C343398A27,
    JSONSchemaValidator709FDa3C42B8877A,
    JSONSchemaValidator33B799D04D0A8907,
    JSONSchemaValidator7Aa3Da9D4E098Ef2,
    JSONSchemaValidator63Bb88B74F59Aa17,
    JSONSchemaValidator9788B8Fc4418831D,
    JSONSchemaValidator948EA8194348Bc0B,
    JSONSchemaValidator47A1B84B4E1B8044,
    JSONSchemaValidator99872A134D0A9Fb4,
    JSONSchemaValidatorA5Ac99774C6BB541,
    JSONSchemaValidatorA4967Be64DfaAa1A,
    JSONSchemaValidatorA6B798Ab4AcaA34E,
    JSONSchemaValidator58A3699E489B9529,
    JSONSchemaValidatorB68A6Bd8473A9A25,
    JSONSchemaValidatorC1Ba9A424C08A01B,
    JSONSchemaValidatorBf859Ac64A0BA19C,
    JSONSchemaValidatorC5AcD9Fa4C1A8Abc,
    JSONSchemaValidatorDb8E09234A988Bab,
    JSONSchemaValidatorF5Ac590C4Ca9975A,
    JSONSchemaValidator89B36B4649999D81,
    JSONSchemaValidatorFba0D80747Eb82E8,
    JSONSchemaValidator979688084B7BA60D,
    JSONSchemaValidatorA6965B454C9A8663,
    JSONSchemaValidatorF6Ac994F451BA011,
    JSONSchemaValidatorFf816B8E435897Eb,
    JSONSchemaValidator26B44Ab04649A183,
    JSONSchemaValidatorA1A9387346Ba92B1,
    JSONSchemaValidatorE78BB8A2449B9Eed,
    JSONSchemaValidatorF5A269C44F2A95Fa,
    JSONSchemaValidatorE487F8D3481B94F2,
    JSONSchemaValidator33Bb2B9D40199E14,
    JSONSchemaValidatorD6B8Ca774739Adf4,
    JSONSchemaValidator3F89Bbfc4F6B8B50,
    JSONSchemaValidator42B6A86E44B8Bdfc,
    JSONSchemaValidator9698C8Ec4A0B8C1A,
    JSONSchemaValidator55Bc3Bf94E38B6Ff,
    JSONSchemaValidator8A9D2B76443B914E,
    JSONSchemaValidatorA395Fae644Ca899C,
    JSONSchemaValidator7Ab9A8Bd4F3B86A4,
    JSONSchemaValidator0C8F7A0B49B9Aedd,
    JSONSchemaValidator8Cb6783B4FabA1F4,
    JSONSchemaValidator4Dbe3Bc743A891Bc,
    JSONSchemaValidatorBc8AAb4746Ca883D,
    JSONSchemaValidatorFb9BEb664F2ABa4C,
    JSONSchemaValidator0A9C988445Cb91C8,
    JSONSchemaValidator21A6Db2540298F55,
    JSONSchemaValidator3086C9624F498B85,
    JSONSchemaValidator0B836B7B4B6A9Fd5,
    JSONSchemaValidator1E962Af345B8B59F,
    JSONSchemaValidator09B0F9Ce4239Ae10,
    JSONSchemaValidator5889Fb844939A13B,
    JSONSchemaValidator2499E9Ad42E8Ae5B,
    JSONSchemaValidator3Cb24Acb486B89D2,
    JSONSchemaValidator80AcB88E4Ac9Ac6D,
    JSONSchemaValidator6F9819E84178870C,
    JSONSchemaValidator7989F86846FaAf99,
    JSONSchemaValidator8Da0391947088A5A,
    JSONSchemaValidator7E92F9Eb46Db8320,
    JSONSchemaValidator9E857B5A4A0BBcdb,
    JSONSchemaValidatorA4B6C87A4Ffb9Efa,
    JSONSchemaValidatorAeb4Dad04A99Bbe3,
    JSONSchemaValidatorAf8D7B0E470B8Ae2,
    JSONSchemaValidatorBab6C9E5440885Cc,
    JSONSchemaValidator70A479A6462A9496,
    JSONSchemaValidatorCf9418234D9AB37E,
    JSONSchemaValidatorD8A619974A8A8C48,
    JSONSchemaValidatorE6B3Db8046C99654,
    JSONSchemaValidator848B5A7B4F9B8C12,
    JSONSchemaValidatorD9A1Fa9C4068B23C,
    JSONSchemaValidatorF09319674049A7D4,
    JSONSchemaValidatorCdab9B474899Ae06,
    JSONSchemaValidatorF3B26B5544CaBab9,
    JSONSchemaValidator7Fbe4B804879Baa4,
    JSONSchemaValidator828828F44F28Bd0D,
    JSONSchemaValidator0Db7Da744C0B83D8,
    JSONSchemaValidator3D923B184Dc9A4Ca,
    JSONSchemaValidator3B9EF9674429Be4C,
    JSONSchemaValidator20B19B52464B8972,
    JSONSchemaValidator38Bd0B884B89A785,
    JSONSchemaValidator5Db21B8E43FaB7D8,
    JSONSchemaValidator288DF9494F2A9746,
    JSONSchemaValidator349C888443B89A58,
    JSONSchemaValidator1C894B5848EaB214,
    JSONSchemaValidator84B33A9E480ABcaf,
    JSONSchemaValidator4Bb22Af046Fa8F08,
    JSONSchemaValidator888F585C49B88441,
    JSONSchemaValidator4Eb56A614Cc9A2D2,
    JSONSchemaValidator82918A1B4D289C5C,
    JSONSchemaValidator8Db939744649A782,
    JSONSchemaValidator5B8639224Cd88Ea7,
    JSONSchemaValidator84B37Ae54C59Ab28,
    JSONSchemaValidator70Ad397649E9B4D3,
    JSONSchemaValidator81Bb4804405A8D2F,
    JSONSchemaValidator84Ad8B0E42CaB48A,
    JSONSchemaValidatorB7BcAa084E2B90D0,
    JSONSchemaValidatorB9855Ad54Ae98156,
    JSONSchemaValidatorBa9DC85B4B8A9A17,
    JSONSchemaValidatorCd8469E647CaAb0E,
    JSONSchemaValidatorD0A4B88145AaBb51,
    JSONSchemaValidator819F9Aa54FeaB7Bf,
    JSONSchemaValidator8Fa8Eb404A4A8D96,
    JSONSchemaValidatorF5947A4C439A8Bf0,
    JSONSchemaValidatorAeb9Eb67460B92Df,
    JSONSchemaValidatorB888792D43BaBa46,
    JSONSchemaValidatorC3B3C9Ef4E6B8A09,
    JSONSchemaValidatorC9809B6744F8A502,
    JSONSchemaValidatorD888Ab6D4D59A8C1,
    JSONSchemaValidatorCd98780F4888A66D,
    JSONSchemaValidatorF49548C54Be8A3E2,
    JSONSchemaValidatorFfa748Cc44E9A437,
    JSONSchemaValidatorEb8249E34F69B0F1,
    JSONSchemaValidatorF6826A8E41BbA242,
    JSONSchemaValidator89B2Fb144F5BB09B,
    JSONSchemaValidator17A82Ac94Cf99Ab0,
    JSONSchemaValidatorEeb168Eb41988E07,
    JSONSchemaValidator50B589Fd4C7A930A,
    JSONSchemaValidator6284Db4649Aa8D31,
    JSONSchemaValidator9Ba14A9E441B8A60,
    JSONSchemaValidatorB2B8Cb91459AA58F,
    JSONSchemaValidatorC2B5Fb764D888375,
    JSONSchemaValidatorB9B48Ac8463A8Aba,
    JSONSchemaValidatorCa91Da84401ABba1,
    JSONSchemaValidator149AA93B4Ddb80Dd,
    JSONSchemaValidatorE2AdBa7943BaB3E9,
    JSONSchemaValidatorAc8AE94C4E69A09D,
    JSONSchemaValidatorCca098344A489Dfa,
    JSONSchemaValidator8A96Fb954D09A349,
    JSONSchemaValidatorDb9F997F4E59Aec1,
    JSONSchemaValidatorC7A6592B4B98A369,
    JSONSchemaValidatorCca519Ba45EbB423,
    JSONSchemaValidator98A39Bf4485A9871,
    JSONSchemaValidatorBead7B3443B996A7,
    JSONSchemaValidatorCb81B93540BaAab0,
    json_schema_validate
)


__version__ = get_versions()['version']
del get_versions


# Initialize Package Logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
