# -*- coding: utf-8 -*-
"""Validates DNA Center JSON request objects.

Classes:
    SchemaValidator: Validates DNA Center JSON request objects.

The SchemaValidator class validates any dict structure passed by
the user with the JSON schema of the request.

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

from builtins import *
import json
from collections import defaultdict

import fastjsonschema
from dnacentersdk.exceptions import MalformedRequest

from .validators.jsd_01b09a254b9ab259 \
    import JSONSchemaValidator01B09A254B9AB259
from .validators.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E
from .validators.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342
from .validators.jsd_109d1b4f4289aecd \
    import JSONSchemaValidator109D1B4F4289Aecd
from .validators.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A
from .validators.jsd_83a3b9404cb88787 \
    import JSONSchemaValidator83A3B9404Cb88787
from .validators.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254
from .validators.jsd_9c9a785741cbb41f \
    import JSONSchemaValidator9C9A785741CbB41F
from .validators.jsd_a7b42836408a8e74 \
    import JSONSchemaValidatorA7B42836408A8E74
from .validators.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216
from .validators.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48
from .validators.jsd_d0a1abfa435b841d \
    import JSONSchemaValidatorD0A1Abfa435B841D
from .validators.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16
from .validators.jsd_c8bf6b65414a9bc7 \
    import JSONSchemaValidatorC8Bf6B65414A9Bc7
from .validators.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317
from .validators.jsd_2e9db85840fbb1cf \
    import JSONSchemaValidator2E9DB85840FbB1Cf
from .validators.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64
from .validators.jsd_4695090d403b8eaa \
    import JSONSchemaValidator4695090D403B8Eaa
from .validators.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E
from .validators.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9
from .validators.jsd_8091a9b84bfba53b \
    import JSONSchemaValidator8091A9B84BfbA53B
from .validators.jsd_429c28154bdaa13d \
    import JSONSchemaValidator429C28154BdaA13D
from .validators.jsd_caa3ea704d78b37e \
    import JSONSchemaValidatorCaa3Ea704D78B37E
from .validators.jsd_eab7abe048fb99ad \
    import JSONSchemaValidatorEab7Abe048Fb99Ad
from .validators.jsd_c1a359b14c89b573 \
    import JSONSchemaValidatorC1A359B14C89B573
from .validators.jsd_ee9aab01487a8896 \
    import JSONSchemaValidatorEe9AAb01487A8896
from .validators.jsd_069d9823451b892d \
    import JSONSchemaValidator069D9823451B892D
from .validators.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564
from .validators.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb
from .validators.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe
from .validators.jsd_44974ba5435a801d \
    import JSONSchemaValidator44974Ba5435A801D
from .validators.jsd_4c8cab5f435a80f4 \
    import JSONSchemaValidator4C8CAb5F435A80F4
from .validators.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140
from .validators.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7
from .validators.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24
from .validators.jsd_3d9b99c343398a27 \
    import JSONSchemaValidator3D9B99C343398A27
from .validators.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A
from .validators.jsd_33b799d04d0a8907 \
    import JSONSchemaValidator33B799D04D0A8907
from .validators.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2
from .validators.jsd_63bb88b74f59aa17 \
    import JSONSchemaValidator63Bb88B74F59Aa17
from .validators.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D
from .validators.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B
from .validators.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044
from .validators.jsd_99872a134d0a9fb4 \
    import JSONSchemaValidator99872A134D0A9Fb4
from .validators.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541
from .validators.jsd_a4967be64dfaaa1a \
    import JSONSchemaValidatorA4967Be64DfaAa1A
from .validators.jsd_a6b798ab4acaa34e \
    import JSONSchemaValidatorA6B798Ab4AcaA34E
from .validators.jsd_58a3699e489b9529 \
    import JSONSchemaValidator58A3699E489B9529
from .validators.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25
from .validators.jsd_c1ba9a424c08a01b \
    import JSONSchemaValidatorC1Ba9A424C08A01B
from .validators.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C
from .validators.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc
from .validators.jsd_db8e09234a988bab \
    import JSONSchemaValidatorDb8E09234A988Bab
from .validators.jsd_f5ac590c4ca9975a \
    import JSONSchemaValidatorF5Ac590C4Ca9975A
from .validators.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81
from .validators.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8
from .validators.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D
from .validators.jsd_a6965b454c9a8663 \
    import JSONSchemaValidatorA6965B454C9A8663
from .validators.jsd_f6ac994f451ba011 \
    import JSONSchemaValidatorF6Ac994F451BA011
from .validators.jsd_ff816b8e435897eb \
    import JSONSchemaValidatorFf816B8E435897Eb
from .validators.jsd_26b44ab04649a183 \
    import JSONSchemaValidator26B44Ab04649A183
from .validators.jsd_a1a9387346ba92b1 \
    import JSONSchemaValidatorA1A9387346Ba92B1
from .validators.jsd_e78bb8a2449b9eed \
    import JSONSchemaValidatorE78BB8A2449B9Eed
from .validators.jsd_f5a269c44f2a95fa \
    import JSONSchemaValidatorF5A269C44F2A95Fa
from .validators.jsd_e487f8d3481b94f2 \
    import JSONSchemaValidatorE487F8D3481B94F2
from .validators.jsd_33bb2b9d40199e14 \
    import JSONSchemaValidator33Bb2B9D40199E14
from .validators.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4
from .validators.jsd_3f89bbfc4f6b8b50 \
    import JSONSchemaValidator3F89Bbfc4F6B8B50
from .validators.jsd_42b6a86e44b8bdfc \
    import JSONSchemaValidator42B6A86E44B8Bdfc
from .validators.jsd_9698c8ec4a0b8c1a \
    import JSONSchemaValidator9698C8Ec4A0B8C1A
from .validators.jsd_55bc3bf94e38b6ff \
    import JSONSchemaValidator55Bc3Bf94E38B6Ff
from .validators.jsd_8a9d2b76443b914e \
    import JSONSchemaValidator8A9D2B76443B914E
from .validators.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C
from .validators.jsd_7ab9a8bd4f3b86a4 \
    import JSONSchemaValidator7Ab9A8Bd4F3B86A4
from .validators.jsd_0c8f7a0b49b9aedd \
    import JSONSchemaValidator0C8F7A0B49B9Aedd
from .validators.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4
from .validators.jsd_4dbe3bc743a891bc \
    import JSONSchemaValidator4Dbe3Bc743A891Bc
from .validators.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D
from .validators.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C
from .validators.jsd_0a9c988445cb91c8 \
    import JSONSchemaValidator0A9C988445Cb91C8
from .validators.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55
from .validators.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85
from .validators.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5
from .validators.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F
from .validators.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10
from .validators.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B
from .validators.jsd_2499e9ad42e8ae5b \
    import JSONSchemaValidator2499E9Ad42E8Ae5B
from .validators.jsd_3cb24acb486b89d2 \
    import JSONSchemaValidator3Cb24Acb486B89D2
from .validators.jsd_80acb88e4ac9ac6d \
    import JSONSchemaValidator80AcB88E4Ac9Ac6D
from .validators.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C
from .validators.jsd_7989f86846faaf99 \
    import JSONSchemaValidator7989F86846FaAf99
from .validators.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A
from .validators.jsd_7e92f9eb46db8320 \
    import JSONSchemaValidator7E92F9Eb46Db8320
from .validators.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb
from .validators.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa
from .validators.jsd_aeb4dad04a99bbe3 \
    import JSONSchemaValidatorAeb4Dad04A99Bbe3
from .validators.jsd_af8d7b0e470b8ae2 \
    import JSONSchemaValidatorAf8D7B0E470B8Ae2
from .validators.jsd_bab6c9e5440885cc \
    import JSONSchemaValidatorBab6C9E5440885Cc
from .validators.jsd_70a479a6462a9496 \
    import JSONSchemaValidator70A479A6462A9496
from .validators.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E
from .validators.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48
from .validators.jsd_e6b3db8046c99654 \
    import JSONSchemaValidatorE6B3Db8046C99654
from .validators.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12
from .validators.jsd_d9a1fa9c4068b23c \
    import JSONSchemaValidatorD9A1Fa9C4068B23C
from .validators.jsd_f09319674049a7d4 \
    import JSONSchemaValidatorF09319674049A7D4
from .validators.jsd_cdab9b474899ae06 \
    import JSONSchemaValidatorCdab9B474899Ae06
from .validators.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9
from .validators.jsd_7fbe4b804879baa4 \
    import JSONSchemaValidator7Fbe4B804879Baa4
from .validators.jsd_828828f44f28bd0d \
    import JSONSchemaValidator828828F44F28Bd0D
from .validators.jsd_0db7da744c0b83d8 \
    import JSONSchemaValidator0Db7Da744C0B83D8
from .validators.jsd_3d923b184dc9a4ca \
    import JSONSchemaValidator3D923B184Dc9A4Ca
from .validators.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C
from .validators.jsd_20b19b52464b8972 \
    import JSONSchemaValidator20B19B52464B8972
from .validators.jsd_38bd0b884b89a785 \
    import JSONSchemaValidator38Bd0B884B89A785
from .validators.jsd_5db21b8e43fab7d8 \
    import JSONSchemaValidator5Db21B8E43FaB7D8
from .validators.jsd_288df9494f2a9746 \
    import JSONSchemaValidator288DF9494F2A9746
from .validators.jsd_349c888443b89a58 \
    import JSONSchemaValidator349C888443B89A58
from .validators.jsd_1c894b5848eab214 \
    import JSONSchemaValidator1C894B5848EaB214
from .validators.jsd_84b33a9e480abcaf \
    import JSONSchemaValidator84B33A9E480ABcaf
from .validators.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08
from .validators.jsd_888f585c49b88441 \
    import JSONSchemaValidator888F585C49B88441
from .validators.jsd_4eb56a614cc9a2d2 \
    import JSONSchemaValidator4Eb56A614Cc9A2D2
from .validators.jsd_82918a1b4d289c5c \
    import JSONSchemaValidator82918A1B4D289C5C
from .validators.jsd_8db939744649a782 \
    import JSONSchemaValidator8Db939744649A782
from .validators.jsd_5b8639224cd88ea7 \
    import JSONSchemaValidator5B8639224Cd88Ea7
from .validators.jsd_84b37ae54c59ab28 \
    import JSONSchemaValidator84B37Ae54C59Ab28
from .validators.jsd_70ad397649e9b4d3 \
    import JSONSchemaValidator70Ad397649E9B4D3
from .validators.jsd_81bb4804405a8d2f \
    import JSONSchemaValidator81Bb4804405A8D2F
from .validators.jsd_84ad8b0e42cab48a \
    import JSONSchemaValidator84Ad8B0E42CaB48A
from .validators.jsd_b7bcaa084e2b90d0 \
    import JSONSchemaValidatorB7BcAa084E2B90D0
from .validators.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156
from .validators.jsd_ba9dc85b4b8a9a17 \
    import JSONSchemaValidatorBa9DC85B4B8A9A17
from .validators.jsd_cd8469e647caab0e \
    import JSONSchemaValidatorCd8469E647CaAb0E
from .validators.jsd_d0a4b88145aabb51 \
    import JSONSchemaValidatorD0A4B88145AaBb51
from .validators.jsd_819f9aa54feab7bf \
    import JSONSchemaValidator819F9Aa54FeaB7Bf
from .validators.jsd_8fa8eb404a4a8d96 \
    import JSONSchemaValidator8Fa8Eb404A4A8D96
from .validators.jsd_f5947a4c439a8bf0 \
    import JSONSchemaValidatorF5947A4C439A8Bf0
from .validators.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df
from .validators.jsd_b888792d43baba46 \
    import JSONSchemaValidatorB888792D43BaBa46
from .validators.jsd_c3b3c9ef4e6b8a09 \
    import JSONSchemaValidatorC3B3C9Ef4E6B8A09
from .validators.jsd_c9809b6744f8a502 \
    import JSONSchemaValidatorC9809B6744F8A502
from .validators.jsd_d888ab6d4d59a8c1 \
    import JSONSchemaValidatorD888Ab6D4D59A8C1
from .validators.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D
from .validators.jsd_f49548c54be8a3e2 \
    import JSONSchemaValidatorF49548C54Be8A3E2
from .validators.jsd_ffa748cc44e9a437 \
    import JSONSchemaValidatorFfa748Cc44E9A437
from .validators.jsd_eb8249e34f69b0f1 \
    import JSONSchemaValidatorEb8249E34F69B0F1
from .validators.jsd_f6826a8e41bba242 \
    import JSONSchemaValidatorF6826A8E41BbA242
from .validators.jsd_89b2fb144f5bb09b \
    import JSONSchemaValidator89B2Fb144F5BB09B
from .validators.jsd_17a82ac94cf99ab0 \
    import JSONSchemaValidator17A82Ac94Cf99Ab0
from .validators.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07
from .validators.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A
from .validators.jsd_6284db4649aa8d31 \
    import JSONSchemaValidator6284Db4649Aa8D31
from .validators.jsd_9ba14a9e441b8a60 \
    import JSONSchemaValidator9Ba14A9E441B8A60
from .validators.jsd_b2b8cb91459aa58f \
    import JSONSchemaValidatorB2B8Cb91459AA58F
from .validators.jsd_c2b5fb764d888375 \
    import JSONSchemaValidatorC2B5Fb764D888375
from .validators.jsd_b9b48ac8463a8aba \
    import JSONSchemaValidatorB9B48Ac8463A8Aba
from .validators.jsd_ca91da84401abba1 \
    import JSONSchemaValidatorCa91Da84401ABba1
from .validators.jsd_149aa93b4ddb80dd \
    import JSONSchemaValidator149AA93B4Ddb80Dd
from .validators.jsd_e2adba7943bab3e9 \
    import JSONSchemaValidatorE2AdBa7943BaB3E9
from .validators.jsd_ac8ae94c4e69a09d \
    import JSONSchemaValidatorAc8AE94C4E69A09D
from .validators.jsd_cca098344a489dfa \
    import JSONSchemaValidatorCca098344A489Dfa
from .validators.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349
from .validators.jsd_db9f997f4e59aec1 \
    import JSONSchemaValidatorDb9F997F4E59Aec1
from .validators.jsd_c7a6592b4b98a369 \
    import JSONSchemaValidatorC7A6592B4B98A369
from .validators.jsd_cca519ba45ebb423 \
    import JSONSchemaValidatorCca519Ba45EbB423
from .validators.jsd_98a39bf4485a9871 \
    import JSONSchemaValidator98A39Bf4485A9871
from .validators.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7
from .validators.jsd_cb81b93540baaab0 \
    import JSONSchemaValidatorCb81B93540BaAab0


class JSONSchemaValidator(object):
    """Validates a DNA Center JSON request."""

    def __init__(self):
        super(JSONSchemaValidator, self).__init__()
        self._validator = fastjsonschema.compile({})

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(
                request, e.message
            ))


json_schema_validators = defaultdict(
    lambda: JSONSchemaValidator,
    jsd_01b09a254b9ab259=JSONSchemaValidator01B09A254B9AB259(),
    jsd_00aec9b1422ab27e=JSONSchemaValidator00AeC9B1422AB27E(),
    jsd_7781fa0548a98342=JSONSchemaValidator7781Fa0548A98342(),
    jsd_109d1b4f4289aecd=JSONSchemaValidator109D1B4F4289Aecd(),
    jsd_6099da82477b858a=JSONSchemaValidator6099Da82477B858A(),
    jsd_83a3b9404cb88787=JSONSchemaValidator83A3B9404Cb88787(),
    jsd_9480fa1f47ca9254=JSONSchemaValidator9480Fa1F47Ca9254(),
    jsd_9c9a785741cbb41f=JSONSchemaValidator9C9A785741CbB41F(),
    jsd_a7b42836408a8e74=JSONSchemaValidatorA7B42836408A8E74(),
    jsd_62b05b2c40a9b216=JSONSchemaValidator62B05B2C40A9B216(),
    jsd_f393abe84989bb48=JSONSchemaValidatorF393Abe84989Bb48(),
    jsd_d0a1abfa435b841d=JSONSchemaValidatorD0A1Abfa435B841D(),
    jsd_f6b119ad4d4aaf16=JSONSchemaValidatorF6B119Ad4D4AAf16(),
    jsd_c8bf6b65414a9bc7=JSONSchemaValidatorC8Bf6B65414A9Bc7(),
    jsd_00a2fa6146089317=JSONSchemaValidator00A2Fa6146089317(),
    jsd_2e9db85840fbb1cf=JSONSchemaValidator2E9DB85840FbB1Cf(),
    jsd_1399891c42a8be64=JSONSchemaValidator1399891C42A8Be64(),
    jsd_4695090d403b8eaa=JSONSchemaValidator4695090D403B8Eaa(),
    jsd_45bc7a8344a8bc1e=JSONSchemaValidator45Bc7A8344A8Bc1E(),
    jsd_4d86a993469a9da9=JSONSchemaValidator4D86A993469A9Da9(),
    jsd_8091a9b84bfba53b=JSONSchemaValidator8091A9B84BfbA53B(),
    jsd_429c28154bdaa13d=JSONSchemaValidator429C28154BdaA13D(),
    jsd_caa3ea704d78b37e=JSONSchemaValidatorCaa3Ea704D78B37E(),
    jsd_eab7abe048fb99ad=JSONSchemaValidatorEab7Abe048Fb99Ad(),
    jsd_c1a359b14c89b573=JSONSchemaValidatorC1A359B14C89B573(),
    jsd_ee9aab01487a8896=JSONSchemaValidatorEe9AAb01487A8896(),
    jsd_069d9823451b892d=JSONSchemaValidator069D9823451B892D(),
    jsd_17929bc7465bb564=JSONSchemaValidator17929Bc7465BB564(),
    jsd_10b06a6a4f7bb3cb=JSONSchemaValidator10B06A6A4F7BB3Cb(),
    jsd_1da5ebdd434aacfe=JSONSchemaValidator1Da5Ebdd434AAcfe(),
    jsd_44974ba5435a801d=JSONSchemaValidator44974Ba5435A801D(),
    jsd_4c8cab5f435a80f4=JSONSchemaValidator4C8CAb5F435A80F4(),
    jsd_55b439dc4239b140=JSONSchemaValidator55B439Dc4239B140(),
    jsd_6bacb8d14639bdc7=JSONSchemaValidator6BacB8D14639Bdc7(),
    jsd_4d9ca8e2431a8a24=JSONSchemaValidator4D9CA8E2431A8A24(),
    jsd_3d9b99c343398a27=JSONSchemaValidator3D9B99C343398A27(),
    jsd_709fda3c42b8877a=JSONSchemaValidator709FDa3C42B8877A(),
    jsd_33b799d04d0a8907=JSONSchemaValidator33B799D04D0A8907(),
    jsd_7aa3da9d4e098ef2=JSONSchemaValidator7Aa3Da9D4E098Ef2(),
    jsd_63bb88b74f59aa17=JSONSchemaValidator63Bb88B74F59Aa17(),
    jsd_9788b8fc4418831d=JSONSchemaValidator9788B8Fc4418831D(),
    jsd_948ea8194348bc0b=JSONSchemaValidator948EA8194348Bc0B(),
    jsd_47a1b84b4e1b8044=JSONSchemaValidator47A1B84B4E1B8044(),
    jsd_99872a134d0a9fb4=JSONSchemaValidator99872A134D0A9Fb4(),
    jsd_a5ac99774c6bb541=JSONSchemaValidatorA5Ac99774C6BB541(),
    jsd_a4967be64dfaaa1a=JSONSchemaValidatorA4967Be64DfaAa1A(),
    jsd_a6b798ab4acaa34e=JSONSchemaValidatorA6B798Ab4AcaA34E(),
    jsd_58a3699e489b9529=JSONSchemaValidator58A3699E489B9529(),
    jsd_b68a6bd8473a9a25=JSONSchemaValidatorB68A6Bd8473A9A25(),
    jsd_c1ba9a424c08a01b=JSONSchemaValidatorC1Ba9A424C08A01B(),
    jsd_bf859ac64a0ba19c=JSONSchemaValidatorBf859Ac64A0BA19C(),
    jsd_c5acd9fa4c1a8abc=JSONSchemaValidatorC5AcD9Fa4C1A8Abc(),
    jsd_db8e09234a988bab=JSONSchemaValidatorDb8E09234A988Bab(),
    jsd_f5ac590c4ca9975a=JSONSchemaValidatorF5Ac590C4Ca9975A(),
    jsd_89b36b4649999d81=JSONSchemaValidator89B36B4649999D81(),
    jsd_fba0d80747eb82e8=JSONSchemaValidatorFba0D80747Eb82E8(),
    jsd_979688084b7ba60d=JSONSchemaValidator979688084B7BA60D(),
    jsd_a6965b454c9a8663=JSONSchemaValidatorA6965B454C9A8663(),
    jsd_f6ac994f451ba011=JSONSchemaValidatorF6Ac994F451BA011(),
    jsd_ff816b8e435897eb=JSONSchemaValidatorFf816B8E435897Eb(),
    jsd_26b44ab04649a183=JSONSchemaValidator26B44Ab04649A183(),
    jsd_a1a9387346ba92b1=JSONSchemaValidatorA1A9387346Ba92B1(),
    jsd_e78bb8a2449b9eed=JSONSchemaValidatorE78BB8A2449B9Eed(),
    jsd_f5a269c44f2a95fa=JSONSchemaValidatorF5A269C44F2A95Fa(),
    jsd_e487f8d3481b94f2=JSONSchemaValidatorE487F8D3481B94F2(),
    jsd_33bb2b9d40199e14=JSONSchemaValidator33Bb2B9D40199E14(),
    jsd_d6b8ca774739adf4=JSONSchemaValidatorD6B8Ca774739Adf4(),
    jsd_3f89bbfc4f6b8b50=JSONSchemaValidator3F89Bbfc4F6B8B50(),
    jsd_42b6a86e44b8bdfc=JSONSchemaValidator42B6A86E44B8Bdfc(),
    jsd_9698c8ec4a0b8c1a=JSONSchemaValidator9698C8Ec4A0B8C1A(),
    jsd_55bc3bf94e38b6ff=JSONSchemaValidator55Bc3Bf94E38B6Ff(),
    jsd_8a9d2b76443b914e=JSONSchemaValidator8A9D2B76443B914E(),
    jsd_a395fae644ca899c=JSONSchemaValidatorA395Fae644Ca899C(),
    jsd_7ab9a8bd4f3b86a4=JSONSchemaValidator7Ab9A8Bd4F3B86A4(),
    jsd_0c8f7a0b49b9aedd=JSONSchemaValidator0C8F7A0B49B9Aedd(),
    jsd_8cb6783b4faba1f4=JSONSchemaValidator8Cb6783B4FabA1F4(),
    jsd_4dbe3bc743a891bc=JSONSchemaValidator4Dbe3Bc743A891Bc(),
    jsd_bc8aab4746ca883d=JSONSchemaValidatorBc8AAb4746Ca883D(),
    jsd_fb9beb664f2aba4c=JSONSchemaValidatorFb9BEb664F2ABa4C(),
    jsd_0a9c988445cb91c8=JSONSchemaValidator0A9C988445Cb91C8(),
    jsd_21a6db2540298f55=JSONSchemaValidator21A6Db2540298F55(),
    jsd_3086c9624f498b85=JSONSchemaValidator3086C9624F498B85(),
    jsd_0b836b7b4b6a9fd5=JSONSchemaValidator0B836B7B4B6A9Fd5(),
    jsd_1e962af345b8b59f=JSONSchemaValidator1E962Af345B8B59F(),
    jsd_09b0f9ce4239ae10=JSONSchemaValidator09B0F9Ce4239Ae10(),
    jsd_5889fb844939a13b=JSONSchemaValidator5889Fb844939A13B(),
    jsd_2499e9ad42e8ae5b=JSONSchemaValidator2499E9Ad42E8Ae5B(),
    jsd_3cb24acb486b89d2=JSONSchemaValidator3Cb24Acb486B89D2(),
    jsd_80acb88e4ac9ac6d=JSONSchemaValidator80AcB88E4Ac9Ac6D(),
    jsd_6f9819e84178870c=JSONSchemaValidator6F9819E84178870C(),
    jsd_7989f86846faaf99=JSONSchemaValidator7989F86846FaAf99(),
    jsd_8da0391947088a5a=JSONSchemaValidator8Da0391947088A5A(),
    jsd_7e92f9eb46db8320=JSONSchemaValidator7E92F9Eb46Db8320(),
    jsd_9e857b5a4a0bbcdb=JSONSchemaValidator9E857B5A4A0BBcdb(),
    jsd_a4b6c87a4ffb9efa=JSONSchemaValidatorA4B6C87A4Ffb9Efa(),
    jsd_aeb4dad04a99bbe3=JSONSchemaValidatorAeb4Dad04A99Bbe3(),
    jsd_af8d7b0e470b8ae2=JSONSchemaValidatorAf8D7B0E470B8Ae2(),
    jsd_bab6c9e5440885cc=JSONSchemaValidatorBab6C9E5440885Cc(),
    jsd_70a479a6462a9496=JSONSchemaValidator70A479A6462A9496(),
    jsd_cf9418234d9ab37e=JSONSchemaValidatorCf9418234D9AB37E(),
    jsd_d8a619974a8a8c48=JSONSchemaValidatorD8A619974A8A8C48(),
    jsd_e6b3db8046c99654=JSONSchemaValidatorE6B3Db8046C99654(),
    jsd_848b5a7b4f9b8c12=JSONSchemaValidator848B5A7B4F9B8C12(),
    jsd_d9a1fa9c4068b23c=JSONSchemaValidatorD9A1Fa9C4068B23C(),
    jsd_f09319674049a7d4=JSONSchemaValidatorF09319674049A7D4(),
    jsd_cdab9b474899ae06=JSONSchemaValidatorCdab9B474899Ae06(),
    jsd_f3b26b5544cabab9=JSONSchemaValidatorF3B26B5544CaBab9(),
    jsd_7fbe4b804879baa4=JSONSchemaValidator7Fbe4B804879Baa4(),
    jsd_828828f44f28bd0d=JSONSchemaValidator828828F44F28Bd0D(),
    jsd_0db7da744c0b83d8=JSONSchemaValidator0Db7Da744C0B83D8(),
    jsd_3d923b184dc9a4ca=JSONSchemaValidator3D923B184Dc9A4Ca(),
    jsd_3b9ef9674429be4c=JSONSchemaValidator3B9EF9674429Be4C(),
    jsd_20b19b52464b8972=JSONSchemaValidator20B19B52464B8972(),
    jsd_38bd0b884b89a785=JSONSchemaValidator38Bd0B884B89A785(),
    jsd_5db21b8e43fab7d8=JSONSchemaValidator5Db21B8E43FaB7D8(),
    jsd_288df9494f2a9746=JSONSchemaValidator288DF9494F2A9746(),
    jsd_349c888443b89a58=JSONSchemaValidator349C888443B89A58(),
    jsd_1c894b5848eab214=JSONSchemaValidator1C894B5848EaB214(),
    jsd_84b33a9e480abcaf=JSONSchemaValidator84B33A9E480ABcaf(),
    jsd_4bb22af046fa8f08=JSONSchemaValidator4Bb22Af046Fa8F08(),
    jsd_888f585c49b88441=JSONSchemaValidator888F585C49B88441(),
    jsd_4eb56a614cc9a2d2=JSONSchemaValidator4Eb56A614Cc9A2D2(),
    jsd_82918a1b4d289c5c=JSONSchemaValidator82918A1B4D289C5C(),
    jsd_8db939744649a782=JSONSchemaValidator8Db939744649A782(),
    jsd_5b8639224cd88ea7=JSONSchemaValidator5B8639224Cd88Ea7(),
    jsd_84b37ae54c59ab28=JSONSchemaValidator84B37Ae54C59Ab28(),
    jsd_70ad397649e9b4d3=JSONSchemaValidator70Ad397649E9B4D3(),
    jsd_81bb4804405a8d2f=JSONSchemaValidator81Bb4804405A8D2F(),
    jsd_84ad8b0e42cab48a=JSONSchemaValidator84Ad8B0E42CaB48A(),
    jsd_b7bcaa084e2b90d0=JSONSchemaValidatorB7BcAa084E2B90D0(),
    jsd_b9855ad54ae98156=JSONSchemaValidatorB9855Ad54Ae98156(),
    jsd_ba9dc85b4b8a9a17=JSONSchemaValidatorBa9DC85B4B8A9A17(),
    jsd_cd8469e647caab0e=JSONSchemaValidatorCd8469E647CaAb0E(),
    jsd_d0a4b88145aabb51=JSONSchemaValidatorD0A4B88145AaBb51(),
    jsd_819f9aa54feab7bf=JSONSchemaValidator819F9Aa54FeaB7Bf(),
    jsd_8fa8eb404a4a8d96=JSONSchemaValidator8Fa8Eb404A4A8D96(),
    jsd_f5947a4c439a8bf0=JSONSchemaValidatorF5947A4C439A8Bf0(),
    jsd_aeb9eb67460b92df=JSONSchemaValidatorAeb9Eb67460B92Df(),
    jsd_b888792d43baba46=JSONSchemaValidatorB888792D43BaBa46(),
    jsd_c3b3c9ef4e6b8a09=JSONSchemaValidatorC3B3C9Ef4E6B8A09(),
    jsd_c9809b6744f8a502=JSONSchemaValidatorC9809B6744F8A502(),
    jsd_d888ab6d4d59a8c1=JSONSchemaValidatorD888Ab6D4D59A8C1(),
    jsd_cd98780f4888a66d=JSONSchemaValidatorCd98780F4888A66D(),
    jsd_f49548c54be8a3e2=JSONSchemaValidatorF49548C54Be8A3E2(),
    jsd_ffa748cc44e9a437=JSONSchemaValidatorFfa748Cc44E9A437(),
    jsd_eb8249e34f69b0f1=JSONSchemaValidatorEb8249E34F69B0F1(),
    jsd_f6826a8e41bba242=JSONSchemaValidatorF6826A8E41BbA242(),
    jsd_89b2fb144f5bb09b=JSONSchemaValidator89B2Fb144F5BB09B(),
    jsd_17a82ac94cf99ab0=JSONSchemaValidator17A82Ac94Cf99Ab0(),
    jsd_eeb168eb41988e07=JSONSchemaValidatorEeb168Eb41988E07(),
    jsd_50b589fd4c7a930a=JSONSchemaValidator50B589Fd4C7A930A(),
    jsd_6284db4649aa8d31=JSONSchemaValidator6284Db4649Aa8D31(),
    jsd_9ba14a9e441b8a60=JSONSchemaValidator9Ba14A9E441B8A60(),
    jsd_b2b8cb91459aa58f=JSONSchemaValidatorB2B8Cb91459AA58F(),
    jsd_c2b5fb764d888375=JSONSchemaValidatorC2B5Fb764D888375(),
    jsd_b9b48ac8463a8aba=JSONSchemaValidatorB9B48Ac8463A8Aba(),
    jsd_ca91da84401abba1=JSONSchemaValidatorCa91Da84401ABba1(),
    jsd_149aa93b4ddb80dd=JSONSchemaValidator149AA93B4Ddb80Dd(),
    jsd_e2adba7943bab3e9=JSONSchemaValidatorE2AdBa7943BaB3E9(),
    jsd_ac8ae94c4e69a09d=JSONSchemaValidatorAc8AE94C4E69A09D(),
    jsd_cca098344a489dfa=JSONSchemaValidatorCca098344A489Dfa(),
    jsd_8a96fb954d09a349=JSONSchemaValidator8A96Fb954D09A349(),
    jsd_db9f997f4e59aec1=JSONSchemaValidatorDb9F997F4E59Aec1(),
    jsd_c7a6592b4b98a369=JSONSchemaValidatorC7A6592B4B98A369(),
    jsd_cca519ba45ebb423=JSONSchemaValidatorCca519Ba45EbB423(),
    jsd_98a39bf4485a9871=JSONSchemaValidator98A39Bf4485A9871(),
    jsd_bead7b3443b996a7=JSONSchemaValidatorBead7B3443B996A7(),
    jsd_cb81b93540baaab0=JSONSchemaValidatorCb81B93540BaAab0(),
)


def json_schema_validate(model):
    """Factory function for creating JSONSchemaValidator objects.

    Args:
        model(basestring).

        schema(dict).

    Returns:
        JSONSchemaValidator: The created JSONSchemaValidator object.

    Raises:

    """
    return json_schema_validators[model]
