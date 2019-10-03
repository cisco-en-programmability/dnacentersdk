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

import fastjsonschema
from dnacentersdk.exceptions import MalformedRequest

from .validators.v1_2_10.jsd_01b09a254b9ab259 \
    import JSONSchemaValidator01B09A254B9AB259 \
    as JSONSchemaValidator01B09A254B9AB259_v1_2_10
from .validators.v1_2_10.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_2_10
from .validators.v1_2_10.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_2_10
from .validators.v1_2_10.jsd_109d1b4f4289aecd \
    import JSONSchemaValidator109D1B4F4289Aecd \
    as JSONSchemaValidator109D1B4F4289Aecd_v1_2_10
from .validators.v1_2_10.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_2_10
from .validators.v1_2_10.jsd_83a3b9404cb88787 \
    import JSONSchemaValidator83A3B9404Cb88787 \
    as JSONSchemaValidator83A3B9404Cb88787_v1_2_10
from .validators.v1_2_10.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_2_10
from .validators.v1_2_10.jsd_9c9a785741cbb41f \
    import JSONSchemaValidator9C9A785741CbB41F \
    as JSONSchemaValidator9C9A785741CbB41F_v1_2_10
from .validators.v1_2_10.jsd_a7b42836408a8e74 \
    import JSONSchemaValidatorA7B42836408A8E74 \
    as JSONSchemaValidatorA7B42836408A8E74_v1_2_10
from .validators.v1_2_10.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_2_10
from .validators.v1_2_10.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_2_10
from .validators.v1_2_10.jsd_d0a1abfa435b841d \
    import JSONSchemaValidatorD0A1Abfa435B841D \
    as JSONSchemaValidatorD0A1Abfa435B841D_v1_2_10
from .validators.v1_2_10.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_2_10
from .validators.v1_2_10.jsd_c8bf6b65414a9bc7 \
    import JSONSchemaValidatorC8Bf6B65414A9Bc7 \
    as JSONSchemaValidatorC8Bf6B65414A9Bc7_v1_2_10
from .validators.v1_2_10.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_2_10
from .validators.v1_2_10.jsd_2e9db85840fbb1cf \
    import JSONSchemaValidator2E9DB85840FbB1Cf \
    as JSONSchemaValidator2E9DB85840FbB1Cf_v1_2_10
from .validators.v1_2_10.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_2_10
from .validators.v1_2_10.jsd_4695090d403b8eaa \
    import JSONSchemaValidator4695090D403B8Eaa \
    as JSONSchemaValidator4695090D403B8Eaa_v1_2_10
from .validators.v1_2_10.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_2_10
from .validators.v1_2_10.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_2_10
from .validators.v1_2_10.jsd_8091a9b84bfba53b \
    import JSONSchemaValidator8091A9B84BfbA53B \
    as JSONSchemaValidator8091A9B84BfbA53B_v1_2_10
from .validators.v1_2_10.jsd_429c28154bdaa13d \
    import JSONSchemaValidator429C28154BdaA13D \
    as JSONSchemaValidator429C28154BdaA13D_v1_2_10
from .validators.v1_2_10.jsd_caa3ea704d78b37e \
    import JSONSchemaValidatorCaa3Ea704D78B37E \
    as JSONSchemaValidatorCaa3Ea704D78B37E_v1_2_10
from .validators.v1_2_10.jsd_eab7abe048fb99ad \
    import JSONSchemaValidatorEab7Abe048Fb99Ad \
    as JSONSchemaValidatorEab7Abe048Fb99Ad_v1_2_10
from .validators.v1_2_10.jsd_c1a359b14c89b573 \
    import JSONSchemaValidatorC1A359B14C89B573 \
    as JSONSchemaValidatorC1A359B14C89B573_v1_2_10
from .validators.v1_2_10.jsd_ee9aab01487a8896 \
    import JSONSchemaValidatorEe9AAb01487A8896 \
    as JSONSchemaValidatorEe9AAb01487A8896_v1_2_10
from .validators.v1_2_10.jsd_069d9823451b892d \
    import JSONSchemaValidator069D9823451B892D \
    as JSONSchemaValidator069D9823451B892D_v1_2_10
from .validators.v1_2_10.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_2_10
from .validators.v1_2_10.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_2_10
from .validators.v1_2_10.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_2_10
from .validators.v1_2_10.jsd_44974ba5435a801d \
    import JSONSchemaValidator44974Ba5435A801D \
    as JSONSchemaValidator44974Ba5435A801D_v1_2_10
from .validators.v1_2_10.jsd_4c8cab5f435a80f4 \
    import JSONSchemaValidator4C8CAb5F435A80F4 \
    as JSONSchemaValidator4C8CAb5F435A80F4_v1_2_10
from .validators.v1_2_10.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_2_10
from .validators.v1_2_10.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_2_10
from .validators.v1_2_10.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_2_10
from .validators.v1_2_10.jsd_3d9b99c343398a27 \
    import JSONSchemaValidator3D9B99C343398A27 \
    as JSONSchemaValidator3D9B99C343398A27_v1_2_10
from .validators.v1_2_10.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_2_10
from .validators.v1_2_10.jsd_33b799d04d0a8907 \
    import JSONSchemaValidator33B799D04D0A8907 \
    as JSONSchemaValidator33B799D04D0A8907_v1_2_10
from .validators.v1_2_10.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_2_10
from .validators.v1_2_10.jsd_63bb88b74f59aa17 \
    import JSONSchemaValidator63Bb88B74F59Aa17 \
    as JSONSchemaValidator63Bb88B74F59Aa17_v1_2_10
from .validators.v1_2_10.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_2_10
from .validators.v1_2_10.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_2_10
from .validators.v1_2_10.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_2_10
from .validators.v1_2_10.jsd_99872a134d0a9fb4 \
    import JSONSchemaValidator99872A134D0A9Fb4 \
    as JSONSchemaValidator99872A134D0A9Fb4_v1_2_10
from .validators.v1_2_10.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_2_10
from .validators.v1_2_10.jsd_a4967be64dfaaa1a \
    import JSONSchemaValidatorA4967Be64DfaAa1A \
    as JSONSchemaValidatorA4967Be64DfaAa1A_v1_2_10
from .validators.v1_2_10.jsd_a6b798ab4acaa34e \
    import JSONSchemaValidatorA6B798Ab4AcaA34E \
    as JSONSchemaValidatorA6B798Ab4AcaA34E_v1_2_10
from .validators.v1_2_10.jsd_58a3699e489b9529 \
    import JSONSchemaValidator58A3699E489B9529 \
    as JSONSchemaValidator58A3699E489B9529_v1_2_10
from .validators.v1_2_10.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_2_10
from .validators.v1_2_10.jsd_c1ba9a424c08a01b \
    import JSONSchemaValidatorC1Ba9A424C08A01B \
    as JSONSchemaValidatorC1Ba9A424C08A01B_v1_2_10
from .validators.v1_2_10.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_2_10
from .validators.v1_2_10.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_2_10
from .validators.v1_2_10.jsd_db8e09234a988bab \
    import JSONSchemaValidatorDb8E09234A988Bab \
    as JSONSchemaValidatorDb8E09234A988Bab_v1_2_10
from .validators.v1_2_10.jsd_f5ac590c4ca9975a \
    import JSONSchemaValidatorF5Ac590C4Ca9975A \
    as JSONSchemaValidatorF5Ac590C4Ca9975A_v1_2_10
from .validators.v1_2_10.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_2_10
from .validators.v1_2_10.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_2_10
from .validators.v1_2_10.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_2_10
from .validators.v1_2_10.jsd_a6965b454c9a8663 \
    import JSONSchemaValidatorA6965B454C9A8663 \
    as JSONSchemaValidatorA6965B454C9A8663_v1_2_10
from .validators.v1_2_10.jsd_f6ac994f451ba011 \
    import JSONSchemaValidatorF6Ac994F451BA011 \
    as JSONSchemaValidatorF6Ac994F451BA011_v1_2_10
from .validators.v1_2_10.jsd_ff816b8e435897eb \
    import JSONSchemaValidatorFf816B8E435897Eb \
    as JSONSchemaValidatorFf816B8E435897Eb_v1_2_10
from .validators.v1_2_10.jsd_26b44ab04649a183 \
    import JSONSchemaValidator26B44Ab04649A183 \
    as JSONSchemaValidator26B44Ab04649A183_v1_2_10
from .validators.v1_2_10.jsd_a1a9387346ba92b1 \
    import JSONSchemaValidatorA1A9387346Ba92B1 \
    as JSONSchemaValidatorA1A9387346Ba92B1_v1_2_10
from .validators.v1_2_10.jsd_e78bb8a2449b9eed \
    import JSONSchemaValidatorE78BB8A2449B9Eed \
    as JSONSchemaValidatorE78BB8A2449B9Eed_v1_2_10
from .validators.v1_2_10.jsd_f5a269c44f2a95fa \
    import JSONSchemaValidatorF5A269C44F2A95Fa \
    as JSONSchemaValidatorF5A269C44F2A95Fa_v1_2_10
from .validators.v1_2_10.jsd_e487f8d3481b94f2 \
    import JSONSchemaValidatorE487F8D3481B94F2 \
    as JSONSchemaValidatorE487F8D3481B94F2_v1_2_10
from .validators.v1_2_10.jsd_33bb2b9d40199e14 \
    import JSONSchemaValidator33Bb2B9D40199E14 \
    as JSONSchemaValidator33Bb2B9D40199E14_v1_2_10
from .validators.v1_2_10.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_2_10
from .validators.v1_2_10.jsd_3f89bbfc4f6b8b50 \
    import JSONSchemaValidator3F89Bbfc4F6B8B50 \
    as JSONSchemaValidator3F89Bbfc4F6B8B50_v1_2_10
from .validators.v1_2_10.jsd_42b6a86e44b8bdfc \
    import JSONSchemaValidator42B6A86E44B8Bdfc \
    as JSONSchemaValidator42B6A86E44B8Bdfc_v1_2_10
from .validators.v1_2_10.jsd_9698c8ec4a0b8c1a \
    import JSONSchemaValidator9698C8Ec4A0B8C1A \
    as JSONSchemaValidator9698C8Ec4A0B8C1A_v1_2_10
from .validators.v1_2_10.jsd_55bc3bf94e38b6ff \
    import JSONSchemaValidator55Bc3Bf94E38B6Ff \
    as JSONSchemaValidator55Bc3Bf94E38B6Ff_v1_2_10
from .validators.v1_2_10.jsd_8a9d2b76443b914e \
    import JSONSchemaValidator8A9D2B76443B914E \
    as JSONSchemaValidator8A9D2B76443B914E_v1_2_10
from .validators.v1_2_10.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_2_10
from .validators.v1_2_10.jsd_7ab9a8bd4f3b86a4 \
    import JSONSchemaValidator7Ab9A8Bd4F3B86A4 \
    as JSONSchemaValidator7Ab9A8Bd4F3B86A4_v1_2_10
from .validators.v1_2_10.jsd_0c8f7a0b49b9aedd \
    import JSONSchemaValidator0C8F7A0B49B9Aedd \
    as JSONSchemaValidator0C8F7A0B49B9Aedd_v1_2_10
from .validators.v1_2_10.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_2_10
from .validators.v1_2_10.jsd_4dbe3bc743a891bc \
    import JSONSchemaValidator4Dbe3Bc743A891Bc \
    as JSONSchemaValidator4Dbe3Bc743A891Bc_v1_2_10
from .validators.v1_2_10.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_2_10
from .validators.v1_2_10.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_2_10
from .validators.v1_2_10.jsd_0a9c988445cb91c8 \
    import JSONSchemaValidator0A9C988445Cb91C8 \
    as JSONSchemaValidator0A9C988445Cb91C8_v1_2_10
from .validators.v1_2_10.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_2_10
from .validators.v1_2_10.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_2_10
from .validators.v1_2_10.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_2_10
from .validators.v1_2_10.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_2_10
from .validators.v1_2_10.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_2_10
from .validators.v1_2_10.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_2_10
from .validators.v1_2_10.jsd_2499e9ad42e8ae5b \
    import JSONSchemaValidator2499E9Ad42E8Ae5B \
    as JSONSchemaValidator2499E9Ad42E8Ae5B_v1_2_10
from .validators.v1_2_10.jsd_3cb24acb486b89d2 \
    import JSONSchemaValidator3Cb24Acb486B89D2 \
    as JSONSchemaValidator3Cb24Acb486B89D2_v1_2_10
from .validators.v1_2_10.jsd_80acb88e4ac9ac6d \
    import JSONSchemaValidator80AcB88E4Ac9Ac6D \
    as JSONSchemaValidator80AcB88E4Ac9Ac6D_v1_2_10
from .validators.v1_2_10.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_2_10
from .validators.v1_2_10.jsd_7989f86846faaf99 \
    import JSONSchemaValidator7989F86846FaAf99 \
    as JSONSchemaValidator7989F86846FaAf99_v1_2_10
from .validators.v1_2_10.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_2_10
from .validators.v1_2_10.jsd_7e92f9eb46db8320 \
    import JSONSchemaValidator7E92F9Eb46Db8320 \
    as JSONSchemaValidator7E92F9Eb46Db8320_v1_2_10
from .validators.v1_2_10.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_2_10
from .validators.v1_2_10.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_2_10
from .validators.v1_2_10.jsd_aeb4dad04a99bbe3 \
    import JSONSchemaValidatorAeb4Dad04A99Bbe3 \
    as JSONSchemaValidatorAeb4Dad04A99Bbe3_v1_2_10
from .validators.v1_2_10.jsd_af8d7b0e470b8ae2 \
    import JSONSchemaValidatorAf8D7B0E470B8Ae2 \
    as JSONSchemaValidatorAf8D7B0E470B8Ae2_v1_2_10
from .validators.v1_2_10.jsd_bab6c9e5440885cc \
    import JSONSchemaValidatorBab6C9E5440885Cc \
    as JSONSchemaValidatorBab6C9E5440885Cc_v1_2_10
from .validators.v1_2_10.jsd_70a479a6462a9496 \
    import JSONSchemaValidator70A479A6462A9496 \
    as JSONSchemaValidator70A479A6462A9496_v1_2_10
from .validators.v1_2_10.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_2_10
from .validators.v1_2_10.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_2_10
from .validators.v1_2_10.jsd_e6b3db8046c99654 \
    import JSONSchemaValidatorE6B3Db8046C99654 \
    as JSONSchemaValidatorE6B3Db8046C99654_v1_2_10
from .validators.v1_2_10.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_2_10
from .validators.v1_2_10.jsd_d9a1fa9c4068b23c \
    import JSONSchemaValidatorD9A1Fa9C4068B23C \
    as JSONSchemaValidatorD9A1Fa9C4068B23C_v1_2_10
from .validators.v1_2_10.jsd_f09319674049a7d4 \
    import JSONSchemaValidatorF09319674049A7D4 \
    as JSONSchemaValidatorF09319674049A7D4_v1_2_10
from .validators.v1_2_10.jsd_cdab9b474899ae06 \
    import JSONSchemaValidatorCdab9B474899Ae06 \
    as JSONSchemaValidatorCdab9B474899Ae06_v1_2_10
from .validators.v1_2_10.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_2_10
from .validators.v1_2_10.jsd_7fbe4b804879baa4 \
    import JSONSchemaValidator7Fbe4B804879Baa4 \
    as JSONSchemaValidator7Fbe4B804879Baa4_v1_2_10
from .validators.v1_2_10.jsd_828828f44f28bd0d \
    import JSONSchemaValidator828828F44F28Bd0D \
    as JSONSchemaValidator828828F44F28Bd0D_v1_2_10
from .validators.v1_2_10.jsd_0db7da744c0b83d8 \
    import JSONSchemaValidator0Db7Da744C0B83D8 \
    as JSONSchemaValidator0Db7Da744C0B83D8_v1_2_10
from .validators.v1_2_10.jsd_3d923b184dc9a4ca \
    import JSONSchemaValidator3D923B184Dc9A4Ca \
    as JSONSchemaValidator3D923B184Dc9A4Ca_v1_2_10
from .validators.v1_2_10.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_2_10
from .validators.v1_2_10.jsd_20b19b52464b8972 \
    import JSONSchemaValidator20B19B52464B8972 \
    as JSONSchemaValidator20B19B52464B8972_v1_2_10
from .validators.v1_2_10.jsd_38bd0b884b89a785 \
    import JSONSchemaValidator38Bd0B884B89A785 \
    as JSONSchemaValidator38Bd0B884B89A785_v1_2_10
from .validators.v1_2_10.jsd_5db21b8e43fab7d8 \
    import JSONSchemaValidator5Db21B8E43FaB7D8 \
    as JSONSchemaValidator5Db21B8E43FaB7D8_v1_2_10
from .validators.v1_2_10.jsd_288df9494f2a9746 \
    import JSONSchemaValidator288DF9494F2A9746 \
    as JSONSchemaValidator288DF9494F2A9746_v1_2_10
from .validators.v1_2_10.jsd_349c888443b89a58 \
    import JSONSchemaValidator349C888443B89A58 \
    as JSONSchemaValidator349C888443B89A58_v1_2_10
from .validators.v1_2_10.jsd_1c894b5848eab214 \
    import JSONSchemaValidator1C894B5848EaB214 \
    as JSONSchemaValidator1C894B5848EaB214_v1_2_10
from .validators.v1_2_10.jsd_84b33a9e480abcaf \
    import JSONSchemaValidator84B33A9E480ABcaf \
    as JSONSchemaValidator84B33A9E480ABcaf_v1_2_10
from .validators.v1_2_10.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_2_10
from .validators.v1_2_10.jsd_888f585c49b88441 \
    import JSONSchemaValidator888F585C49B88441 \
    as JSONSchemaValidator888F585C49B88441_v1_2_10
from .validators.v1_2_10.jsd_4eb56a614cc9a2d2 \
    import JSONSchemaValidator4Eb56A614Cc9A2D2 \
    as JSONSchemaValidator4Eb56A614Cc9A2D2_v1_2_10
from .validators.v1_2_10.jsd_82918a1b4d289c5c \
    import JSONSchemaValidator82918A1B4D289C5C \
    as JSONSchemaValidator82918A1B4D289C5C_v1_2_10
from .validators.v1_2_10.jsd_8db939744649a782 \
    import JSONSchemaValidator8Db939744649A782 \
    as JSONSchemaValidator8Db939744649A782_v1_2_10
from .validators.v1_2_10.jsd_5b8639224cd88ea7 \
    import JSONSchemaValidator5B8639224Cd88Ea7 \
    as JSONSchemaValidator5B8639224Cd88Ea7_v1_2_10
from .validators.v1_2_10.jsd_84b37ae54c59ab28 \
    import JSONSchemaValidator84B37Ae54C59Ab28 \
    as JSONSchemaValidator84B37Ae54C59Ab28_v1_2_10
from .validators.v1_2_10.jsd_70ad397649e9b4d3 \
    import JSONSchemaValidator70Ad397649E9B4D3 \
    as JSONSchemaValidator70Ad397649E9B4D3_v1_2_10
from .validators.v1_2_10.jsd_81bb4804405a8d2f \
    import JSONSchemaValidator81Bb4804405A8D2F \
    as JSONSchemaValidator81Bb4804405A8D2F_v1_2_10
from .validators.v1_2_10.jsd_84ad8b0e42cab48a \
    import JSONSchemaValidator84Ad8B0E42CaB48A \
    as JSONSchemaValidator84Ad8B0E42CaB48A_v1_2_10
from .validators.v1_2_10.jsd_b7bcaa084e2b90d0 \
    import JSONSchemaValidatorB7BcAa084E2B90D0 \
    as JSONSchemaValidatorB7BcAa084E2B90D0_v1_2_10
from .validators.v1_2_10.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_2_10
from .validators.v1_2_10.jsd_ba9dc85b4b8a9a17 \
    import JSONSchemaValidatorBa9DC85B4B8A9A17 \
    as JSONSchemaValidatorBa9DC85B4B8A9A17_v1_2_10
from .validators.v1_2_10.jsd_cd8469e647caab0e \
    import JSONSchemaValidatorCd8469E647CaAb0E \
    as JSONSchemaValidatorCd8469E647CaAb0E_v1_2_10
from .validators.v1_2_10.jsd_d0a4b88145aabb51 \
    import JSONSchemaValidatorD0A4B88145AaBb51 \
    as JSONSchemaValidatorD0A4B88145AaBb51_v1_2_10
from .validators.v1_2_10.jsd_819f9aa54feab7bf \
    import JSONSchemaValidator819F9Aa54FeaB7Bf \
    as JSONSchemaValidator819F9Aa54FeaB7Bf_v1_2_10
from .validators.v1_2_10.jsd_8fa8eb404a4a8d96 \
    import JSONSchemaValidator8Fa8Eb404A4A8D96 \
    as JSONSchemaValidator8Fa8Eb404A4A8D96_v1_2_10
from .validators.v1_2_10.jsd_f5947a4c439a8bf0 \
    import JSONSchemaValidatorF5947A4C439A8Bf0 \
    as JSONSchemaValidatorF5947A4C439A8Bf0_v1_2_10
from .validators.v1_2_10.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_2_10
from .validators.v1_2_10.jsd_b888792d43baba46 \
    import JSONSchemaValidatorB888792D43BaBa46 \
    as JSONSchemaValidatorB888792D43BaBa46_v1_2_10
from .validators.v1_2_10.jsd_c3b3c9ef4e6b8a09 \
    import JSONSchemaValidatorC3B3C9Ef4E6B8A09 \
    as JSONSchemaValidatorC3B3C9Ef4E6B8A09_v1_2_10
from .validators.v1_2_10.jsd_c9809b6744f8a502 \
    import JSONSchemaValidatorC9809B6744F8A502 \
    as JSONSchemaValidatorC9809B6744F8A502_v1_2_10
from .validators.v1_2_10.jsd_d888ab6d4d59a8c1 \
    import JSONSchemaValidatorD888Ab6D4D59A8C1 \
    as JSONSchemaValidatorD888Ab6D4D59A8C1_v1_2_10
from .validators.v1_2_10.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_2_10
from .validators.v1_2_10.jsd_f49548c54be8a3e2 \
    import JSONSchemaValidatorF49548C54Be8A3E2 \
    as JSONSchemaValidatorF49548C54Be8A3E2_v1_2_10
from .validators.v1_2_10.jsd_ffa748cc44e9a437 \
    import JSONSchemaValidatorFfa748Cc44E9A437 \
    as JSONSchemaValidatorFfa748Cc44E9A437_v1_2_10
from .validators.v1_2_10.jsd_eb8249e34f69b0f1 \
    import JSONSchemaValidatorEb8249E34F69B0F1 \
    as JSONSchemaValidatorEb8249E34F69B0F1_v1_2_10
from .validators.v1_2_10.jsd_f6826a8e41bba242 \
    import JSONSchemaValidatorF6826A8E41BbA242 \
    as JSONSchemaValidatorF6826A8E41BbA242_v1_2_10
from .validators.v1_2_10.jsd_89b2fb144f5bb09b \
    import JSONSchemaValidator89B2Fb144F5BB09B \
    as JSONSchemaValidator89B2Fb144F5BB09B_v1_2_10
from .validators.v1_2_10.jsd_17a82ac94cf99ab0 \
    import JSONSchemaValidator17A82Ac94Cf99Ab0 \
    as JSONSchemaValidator17A82Ac94Cf99Ab0_v1_2_10
from .validators.v1_2_10.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_2_10
from .validators.v1_2_10.jsd_50b589fd4c7a930a \
    import JSONSchemaValidator50B589Fd4C7A930A \
    as JSONSchemaValidator50B589Fd4C7A930A_v1_2_10
from .validators.v1_2_10.jsd_6284db4649aa8d31 \
    import JSONSchemaValidator6284Db4649Aa8D31 \
    as JSONSchemaValidator6284Db4649Aa8D31_v1_2_10
from .validators.v1_2_10.jsd_9ba14a9e441b8a60 \
    import JSONSchemaValidator9Ba14A9E441B8A60 \
    as JSONSchemaValidator9Ba14A9E441B8A60_v1_2_10
from .validators.v1_2_10.jsd_b2b8cb91459aa58f \
    import JSONSchemaValidatorB2B8Cb91459AA58F \
    as JSONSchemaValidatorB2B8Cb91459AA58F_v1_2_10
from .validators.v1_2_10.jsd_c2b5fb764d888375 \
    import JSONSchemaValidatorC2B5Fb764D888375 \
    as JSONSchemaValidatorC2B5Fb764D888375_v1_2_10
from .validators.v1_2_10.jsd_b9b48ac8463a8aba \
    import JSONSchemaValidatorB9B48Ac8463A8Aba \
    as JSONSchemaValidatorB9B48Ac8463A8Aba_v1_2_10
from .validators.v1_2_10.jsd_ca91da84401abba1 \
    import JSONSchemaValidatorCa91Da84401ABba1 \
    as JSONSchemaValidatorCa91Da84401ABba1_v1_2_10
from .validators.v1_2_10.jsd_149aa93b4ddb80dd \
    import JSONSchemaValidator149AA93B4Ddb80Dd \
    as JSONSchemaValidator149AA93B4Ddb80Dd_v1_2_10
from .validators.v1_2_10.jsd_e2adba7943bab3e9 \
    import JSONSchemaValidatorE2AdBa7943BaB3E9 \
    as JSONSchemaValidatorE2AdBa7943BaB3E9_v1_2_10
from .validators.v1_2_10.jsd_ac8ae94c4e69a09d \
    import JSONSchemaValidatorAc8AE94C4E69A09D \
    as JSONSchemaValidatorAc8AE94C4E69A09D_v1_2_10
from .validators.v1_2_10.jsd_cca098344a489dfa \
    import JSONSchemaValidatorCca098344A489Dfa \
    as JSONSchemaValidatorCca098344A489Dfa_v1_2_10
from .validators.v1_2_10.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_2_10
from .validators.v1_2_10.jsd_db9f997f4e59aec1 \
    import JSONSchemaValidatorDb9F997F4E59Aec1 \
    as JSONSchemaValidatorDb9F997F4E59Aec1_v1_2_10
from .validators.v1_2_10.jsd_c7a6592b4b98a369 \
    import JSONSchemaValidatorC7A6592B4B98A369 \
    as JSONSchemaValidatorC7A6592B4B98A369_v1_2_10
from .validators.v1_2_10.jsd_cca519ba45ebb423 \
    import JSONSchemaValidatorCca519Ba45EbB423 \
    as JSONSchemaValidatorCca519Ba45EbB423_v1_2_10
from .validators.v1_2_10.jsd_98a39bf4485a9871 \
    import JSONSchemaValidator98A39Bf4485A9871 \
    as JSONSchemaValidator98A39Bf4485A9871_v1_2_10
from .validators.v1_2_10.jsd_bead7b3443b996a7 \
    import JSONSchemaValidatorBead7B3443B996A7 \
    as JSONSchemaValidatorBead7B3443B996A7_v1_2_10
from .validators.v1_2_10.jsd_cb81b93540baaab0 \
    import JSONSchemaValidatorCb81B93540BaAab0 \
    as JSONSchemaValidatorCb81B93540BaAab0_v1_2_10
from .validators.v1_3_0.jsd_00aec9b1422ab27e \
    import JSONSchemaValidator00AeC9B1422AB27E \
    as JSONSchemaValidator00AeC9B1422AB27E_v1_3_0
from .validators.v1_3_0.jsd_01b09a254b9ab259 \
    import JSONSchemaValidator01B09A254B9AB259 \
    as JSONSchemaValidator01B09A254B9AB259_v1_3_0
from .validators.v1_3_0.jsd_109d1b4f4289aecd \
    import JSONSchemaValidator109D1B4F4289Aecd \
    as JSONSchemaValidator109D1B4F4289Aecd_v1_3_0
from .validators.v1_3_0.jsd_6099da82477b858a \
    import JSONSchemaValidator6099Da82477B858A \
    as JSONSchemaValidator6099Da82477B858A_v1_3_0
from .validators.v1_3_0.jsd_7781fa0548a98342 \
    import JSONSchemaValidator7781Fa0548A98342 \
    as JSONSchemaValidator7781Fa0548A98342_v1_3_0
from .validators.v1_3_0.jsd_9480fa1f47ca9254 \
    import JSONSchemaValidator9480Fa1F47Ca9254 \
    as JSONSchemaValidator9480Fa1F47Ca9254_v1_3_0
from .validators.v1_3_0.jsd_a7b42836408a8e74 \
    import JSONSchemaValidatorA7B42836408A8E74 \
    as JSONSchemaValidatorA7B42836408A8E74_v1_3_0
from .validators.v1_3_0.jsd_f393abe84989bb48 \
    import JSONSchemaValidatorF393Abe84989Bb48 \
    as JSONSchemaValidatorF393Abe84989Bb48_v1_3_0
from .validators.v1_3_0.jsd_c8bf6b65414a9bc7 \
    import JSONSchemaValidatorC8Bf6B65414A9Bc7 \
    as JSONSchemaValidatorC8Bf6B65414A9Bc7_v1_3_0
from .validators.v1_3_0.jsd_62b05b2c40a9b216 \
    import JSONSchemaValidator62B05B2C40A9B216 \
    as JSONSchemaValidator62B05B2C40A9B216_v1_3_0
from .validators.v1_3_0.jsd_83a3b9404cb88787 \
    import JSONSchemaValidator83A3B9404Cb88787 \
    as JSONSchemaValidator83A3B9404Cb88787_v1_3_0
from .validators.v1_3_0.jsd_f6b119ad4d4aaf16 \
    import JSONSchemaValidatorF6B119Ad4D4AAf16 \
    as JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_0
from .validators.v1_3_0.jsd_9c9a785741cbb41f \
    import JSONSchemaValidator9C9A785741CbB41F \
    as JSONSchemaValidator9C9A785741CbB41F_v1_3_0
from .validators.v1_3_0.jsd_d0a1abfa435b841d \
    import JSONSchemaValidatorD0A1Abfa435B841D \
    as JSONSchemaValidatorD0A1Abfa435B841D_v1_3_0
from .validators.v1_3_0.jsd_00a2fa6146089317 \
    import JSONSchemaValidator00A2Fa6146089317 \
    as JSONSchemaValidator00A2Fa6146089317_v1_3_0
from .validators.v1_3_0.jsd_1399891c42a8be64 \
    import JSONSchemaValidator1399891C42A8Be64 \
    as JSONSchemaValidator1399891C42A8Be64_v1_3_0
from .validators.v1_3_0.jsd_429c28154bdaa13d \
    import JSONSchemaValidator429C28154BdaA13D \
    as JSONSchemaValidator429C28154BdaA13D_v1_3_0
from .validators.v1_3_0.jsd_2e9db85840fbb1cf \
    import JSONSchemaValidator2E9DB85840FbB1Cf \
    as JSONSchemaValidator2E9DB85840FbB1Cf_v1_3_0
from .validators.v1_3_0.jsd_4695090d403b8eaa \
    import JSONSchemaValidator4695090D403B8Eaa \
    as JSONSchemaValidator4695090D403B8Eaa_v1_3_0
from .validators.v1_3_0.jsd_45bc7a8344a8bc1e \
    import JSONSchemaValidator45Bc7A8344A8Bc1E \
    as JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_0
from .validators.v1_3_0.jsd_4d86a993469a9da9 \
    import JSONSchemaValidator4D86A993469A9Da9 \
    as JSONSchemaValidator4D86A993469A9Da9_v1_3_0
from .validators.v1_3_0.jsd_8091a9b84bfba53b \
    import JSONSchemaValidator8091A9B84BfbA53B \
    as JSONSchemaValidator8091A9B84BfbA53B_v1_3_0
from .validators.v1_3_0.jsd_c1a359b14c89b573 \
    import JSONSchemaValidatorC1A359B14C89B573 \
    as JSONSchemaValidatorC1A359B14C89B573_v1_3_0
from .validators.v1_3_0.jsd_eab7abe048fb99ad \
    import JSONSchemaValidatorEab7Abe048Fb99Ad \
    as JSONSchemaValidatorEab7Abe048Fb99Ad_v1_3_0
from .validators.v1_3_0.jsd_caa3ea704d78b37e \
    import JSONSchemaValidatorCaa3Ea704D78B37E \
    as JSONSchemaValidatorCaa3Ea704D78B37E_v1_3_0
from .validators.v1_3_0.jsd_ee9aab01487a8896 \
    import JSONSchemaValidatorEe9AAb01487A8896 \
    as JSONSchemaValidatorEe9AAb01487A8896_v1_3_0
from .validators.v1_3_0.jsd_069d9823451b892d \
    import JSONSchemaValidator069D9823451B892D \
    as JSONSchemaValidator069D9823451B892D_v1_3_0
from .validators.v1_3_0.jsd_17929bc7465bb564 \
    import JSONSchemaValidator17929Bc7465BB564 \
    as JSONSchemaValidator17929Bc7465BB564_v1_3_0
from .validators.v1_3_0.jsd_10b06a6a4f7bb3cb \
    import JSONSchemaValidator10B06A6A4F7BB3Cb \
    as JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_0
from .validators.v1_3_0.jsd_1da5ebdd434aacfe \
    import JSONSchemaValidator1Da5Ebdd434AAcfe \
    as JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_0
from .validators.v1_3_0.jsd_47a1b84b4e1b8044 \
    import JSONSchemaValidator47A1B84B4E1B8044 \
    as JSONSchemaValidator47A1B84B4E1B8044_v1_3_0
from .validators.v1_3_0.jsd_33b799d04d0a8907 \
    import JSONSchemaValidator33B799D04D0A8907 \
    as JSONSchemaValidator33B799D04D0A8907_v1_3_0
from .validators.v1_3_0.jsd_3d9b99c343398a27 \
    import JSONSchemaValidator3D9B99C343398A27 \
    as JSONSchemaValidator3D9B99C343398A27_v1_3_0
from .validators.v1_3_0.jsd_4d9ca8e2431a8a24 \
    import JSONSchemaValidator4D9CA8E2431A8A24 \
    as JSONSchemaValidator4D9CA8E2431A8A24_v1_3_0
from .validators.v1_3_0.jsd_44974ba5435a801d \
    import JSONSchemaValidator44974Ba5435A801D \
    as JSONSchemaValidator44974Ba5435A801D_v1_3_0
from .validators.v1_3_0.jsd_4c8cab5f435a80f4 \
    import JSONSchemaValidator4C8CAb5F435A80F4 \
    as JSONSchemaValidator4C8CAb5F435A80F4_v1_3_0
from .validators.v1_3_0.jsd_55b439dc4239b140 \
    import JSONSchemaValidator55B439Dc4239B140 \
    as JSONSchemaValidator55B439Dc4239B140_v1_3_0
from .validators.v1_3_0.jsd_63bb88b74f59aa17 \
    import JSONSchemaValidator63Bb88B74F59Aa17 \
    as JSONSchemaValidator63Bb88B74F59Aa17_v1_3_0
from .validators.v1_3_0.jsd_6bacb8d14639bdc7 \
    import JSONSchemaValidator6BacB8D14639Bdc7 \
    as JSONSchemaValidator6BacB8D14639Bdc7_v1_3_0
from .validators.v1_3_0.jsd_948ea8194348bc0b \
    import JSONSchemaValidator948EA8194348Bc0B \
    as JSONSchemaValidator948EA8194348Bc0B_v1_3_0
from .validators.v1_3_0.jsd_89b36b4649999d81 \
    import JSONSchemaValidator89B36B4649999D81 \
    as JSONSchemaValidator89B36B4649999D81_v1_3_0
from .validators.v1_3_0.jsd_99872a134d0a9fb4 \
    import JSONSchemaValidator99872A134D0A9Fb4 \
    as JSONSchemaValidator99872A134D0A9Fb4_v1_3_0
from .validators.v1_3_0.jsd_979688084b7ba60d \
    import JSONSchemaValidator979688084B7BA60D \
    as JSONSchemaValidator979688084B7BA60D_v1_3_0
from .validators.v1_3_0.jsd_a5ac99774c6bb541 \
    import JSONSchemaValidatorA5Ac99774C6BB541 \
    as JSONSchemaValidatorA5Ac99774C6BB541_v1_3_0
from .validators.v1_3_0.jsd_9788b8fc4418831d \
    import JSONSchemaValidator9788B8Fc4418831D \
    as JSONSchemaValidator9788B8Fc4418831D_v1_3_0
from .validators.v1_3_0.jsd_b68a6bd8473a9a25 \
    import JSONSchemaValidatorB68A6Bd8473A9A25 \
    as JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_0
from .validators.v1_3_0.jsd_c1ba9a424c08a01b \
    import JSONSchemaValidatorC1Ba9A424C08A01B \
    as JSONSchemaValidatorC1Ba9A424C08A01B_v1_3_0
from .validators.v1_3_0.jsd_db8e09234a988bab \
    import JSONSchemaValidatorDb8E09234A988Bab \
    as JSONSchemaValidatorDb8E09234A988Bab_v1_3_0
from .validators.v1_3_0.jsd_a6965b454c9a8663 \
    import JSONSchemaValidatorA6965B454C9A8663 \
    as JSONSchemaValidatorA6965B454C9A8663_v1_3_0
from .validators.v1_3_0.jsd_f5ac590c4ca9975a \
    import JSONSchemaValidatorF5Ac590C4Ca9975A \
    as JSONSchemaValidatorF5Ac590C4Ca9975A_v1_3_0
from .validators.v1_3_0.jsd_fba0d80747eb82e8 \
    import JSONSchemaValidatorFba0D80747Eb82E8 \
    as JSONSchemaValidatorFba0D80747Eb82E8_v1_3_0
from .validators.v1_3_0.jsd_bf859ac64a0ba19c \
    import JSONSchemaValidatorBf859Ac64A0BA19C \
    as JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_0
from .validators.v1_3_0.jsd_c5acd9fa4c1a8abc \
    import JSONSchemaValidatorC5AcD9Fa4C1A8Abc \
    as JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_0
from .validators.v1_3_0.jsd_58a3699e489b9529 \
    import JSONSchemaValidator58A3699E489B9529 \
    as JSONSchemaValidator58A3699E489B9529_v1_3_0
from .validators.v1_3_0.jsd_709fda3c42b8877a \
    import JSONSchemaValidator709FDa3C42B8877A \
    as JSONSchemaValidator709FDa3C42B8877A_v1_3_0
from .validators.v1_3_0.jsd_7aa3da9d4e098ef2 \
    import JSONSchemaValidator7Aa3Da9D4E098Ef2 \
    as JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_0
from .validators.v1_3_0.jsd_a4967be64dfaaa1a \
    import JSONSchemaValidatorA4967Be64DfaAa1A \
    as JSONSchemaValidatorA4967Be64DfaAa1A_v1_3_0
from .validators.v1_3_0.jsd_a6b798ab4acaa34e \
    import JSONSchemaValidatorA6B798Ab4AcaA34E \
    as JSONSchemaValidatorA6B798Ab4AcaA34E_v1_3_0
from .validators.v1_3_0.jsd_ff816b8e435897eb \
    import JSONSchemaValidatorFf816B8E435897Eb \
    as JSONSchemaValidatorFf816B8E435897Eb_v1_3_0
from .validators.v1_3_0.jsd_f6ac994f451ba011 \
    import JSONSchemaValidatorF6Ac994F451BA011 \
    as JSONSchemaValidatorF6Ac994F451BA011_v1_3_0
from .validators.v1_3_0.jsd_26b44ab04649a183 \
    import JSONSchemaValidator26B44Ab04649A183 \
    as JSONSchemaValidator26B44Ab04649A183_v1_3_0
from .validators.v1_3_0.jsd_a1a9387346ba92b1 \
    import JSONSchemaValidatorA1A9387346Ba92B1 \
    as JSONSchemaValidatorA1A9387346Ba92B1_v1_3_0
from .validators.v1_3_0.jsd_e78bb8a2449b9eed \
    import JSONSchemaValidatorE78BB8A2449B9Eed \
    as JSONSchemaValidatorE78BB8A2449B9Eed_v1_3_0
from .validators.v1_3_0.jsd_f5a269c44f2a95fa \
    import JSONSchemaValidatorF5A269C44F2A95Fa \
    as JSONSchemaValidatorF5A269C44F2A95Fa_v1_3_0
from .validators.v1_3_0.jsd_e487f8d3481b94f2 \
    import JSONSchemaValidatorE487F8D3481B94F2 \
    as JSONSchemaValidatorE487F8D3481B94F2_v1_3_0
from .validators.v1_3_0.jsd_33bb2b9d40199e14 \
    import JSONSchemaValidator33Bb2B9D40199E14 \
    as JSONSchemaValidator33Bb2B9D40199E14_v1_3_0
from .validators.v1_3_0.jsd_d6b8ca774739adf4 \
    import JSONSchemaValidatorD6B8Ca774739Adf4 \
    as JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_0
from .validators.v1_3_0.jsd_3f89bbfc4f6b8b50 \
    import JSONSchemaValidator3F89Bbfc4F6B8B50 \
    as JSONSchemaValidator3F89Bbfc4F6B8B50_v1_3_0
from .validators.v1_3_0.jsd_42b6a86e44b8bdfc \
    import JSONSchemaValidator42B6A86E44B8Bdfc \
    as JSONSchemaValidator42B6A86E44B8Bdfc_v1_3_0
from .validators.v1_3_0.jsd_9698c8ec4a0b8c1a \
    import JSONSchemaValidator9698C8Ec4A0B8C1A \
    as JSONSchemaValidator9698C8Ec4A0B8C1A_v1_3_0
from .validators.v1_3_0.jsd_55bc3bf94e38b6ff \
    import JSONSchemaValidator55Bc3Bf94E38B6Ff \
    as JSONSchemaValidator55Bc3Bf94E38B6Ff_v1_3_0
from .validators.v1_3_0.jsd_7ab9a8bd4f3b86a4 \
    import JSONSchemaValidator7Ab9A8Bd4F3B86A4 \
    as JSONSchemaValidator7Ab9A8Bd4F3B86A4_v1_3_0
from .validators.v1_3_0.jsd_8a9d2b76443b914e \
    import JSONSchemaValidator8A9D2B76443B914E \
    as JSONSchemaValidator8A9D2B76443B914E_v1_3_0
from .validators.v1_3_0.jsd_a395fae644ca899c \
    import JSONSchemaValidatorA395Fae644Ca899C \
    as JSONSchemaValidatorA395Fae644Ca899C_v1_3_0
from .validators.v1_3_0.jsd_07913b7f4e1880de \
    import JSONSchemaValidator07913B7F4E1880De \
    as JSONSchemaValidator07913B7F4E1880De_v1_3_0
from .validators.v1_3_0.jsd_20872aec43b9bf50 \
    import JSONSchemaValidator20872Aec43B9Bf50 \
    as JSONSchemaValidator20872Aec43B9Bf50_v1_3_0
from .validators.v1_3_0.jsd_6896993e41b8bd7a \
    import JSONSchemaValidator6896993E41B8Bd7A \
    as JSONSchemaValidator6896993E41B8Bd7A_v1_3_0
from .validators.v1_3_0.jsd_a0be3a2f47ab9f3c \
    import JSONSchemaValidatorA0Be3A2F47Ab9F3C \
    as JSONSchemaValidatorA0Be3A2F47Ab9F3C_v1_3_0
from .validators.v1_3_0.jsd_ae86a8c14b5980b7 \
    import JSONSchemaValidatorAe86A8C14B5980B7 \
    as JSONSchemaValidatorAe86A8C14B5980B7_v1_3_0
from .validators.v1_3_0.jsd_47ba59204e0ab742 \
    import JSONSchemaValidator47Ba59204E0AB742 \
    as JSONSchemaValidator47Ba59204E0AB742_v1_3_0
from .validators.v1_3_0.jsd_db9f997f4e59aec1 \
    import JSONSchemaValidatorDb9F997F4E59Aec1 \
    as JSONSchemaValidatorDb9F997F4E59Aec1_v1_3_0
from .validators.v1_3_0.jsd_c7a6592b4b98a369 \
    import JSONSchemaValidatorC7A6592B4B98A369 \
    as JSONSchemaValidatorC7A6592B4B98A369_v1_3_0
from .validators.v1_3_0.jsd_cca098344a489dfa \
    import JSONSchemaValidatorCca098344A489Dfa \
    as JSONSchemaValidatorCca098344A489Dfa_v1_3_0
from .validators.v1_3_0.jsd_cca519ba45ebb423 \
    import JSONSchemaValidatorCca519Ba45EbB423 \
    as JSONSchemaValidatorCca519Ba45EbB423_v1_3_0
from .validators.v1_3_0.jsd_8a96fb954d09a349 \
    import JSONSchemaValidator8A96Fb954D09A349 \
    as JSONSchemaValidator8A96Fb954D09A349_v1_3_0
from .validators.v1_3_0.jsd_1e80bb50430b8634 \
    import JSONSchemaValidator1E80Bb50430B8634 \
    as JSONSchemaValidator1E80Bb50430B8634_v1_3_0
from .validators.v1_3_0.jsd_a4b56a5f478a97dd \
    import JSONSchemaValidatorA4B56A5F478A97Dd \
    as JSONSchemaValidatorA4B56A5F478A97Dd_v1_3_0
from .validators.v1_3_0.jsd_d0b3593c4a7aaf22 \
    import JSONSchemaValidatorD0B3593C4A7AAf22 \
    as JSONSchemaValidatorD0B3593C4A7AAf22_v1_3_0
from .validators.v1_3_0.jsd_0db7da744c0b83d8 \
    import JSONSchemaValidator0Db7Da744C0B83D8 \
    as JSONSchemaValidator0Db7Da744C0B83D8_v1_3_0
from .validators.v1_3_0.jsd_1c894b5848eab214 \
    import JSONSchemaValidator1C894B5848EaB214 \
    as JSONSchemaValidator1C894B5848EaB214_v1_3_0
from .validators.v1_3_0.jsd_3b9ef9674429be4c \
    import JSONSchemaValidator3B9EF9674429Be4C \
    as JSONSchemaValidator3B9EF9674429Be4C_v1_3_0
from .validators.v1_3_0.jsd_20b19b52464b8972 \
    import JSONSchemaValidator20B19B52464B8972 \
    as JSONSchemaValidator20B19B52464B8972_v1_3_0
from .validators.v1_3_0.jsd_288df9494f2a9746 \
    import JSONSchemaValidator288DF9494F2A9746 \
    as JSONSchemaValidator288DF9494F2A9746_v1_3_0
from .validators.v1_3_0.jsd_38bd0b884b89a785 \
    import JSONSchemaValidator38Bd0B884B89A785 \
    as JSONSchemaValidator38Bd0B884B89A785_v1_3_0
from .validators.v1_3_0.jsd_349c888443b89a58 \
    import JSONSchemaValidator349C888443B89A58 \
    as JSONSchemaValidator349C888443B89A58_v1_3_0
from .validators.v1_3_0.jsd_3d923b184dc9a4ca \
    import JSONSchemaValidator3D923B184Dc9A4Ca \
    as JSONSchemaValidator3D923B184Dc9A4Ca_v1_3_0
from .validators.v1_3_0.jsd_4bb22af046fa8f08 \
    import JSONSchemaValidator4Bb22Af046Fa8F08 \
    as JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_0
from .validators.v1_3_0.jsd_4eb56a614cc9a2d2 \
    import JSONSchemaValidator4Eb56A614Cc9A2D2 \
    as JSONSchemaValidator4Eb56A614Cc9A2D2_v1_3_0
from .validators.v1_3_0.jsd_5b8639224cd88ea7 \
    import JSONSchemaValidator5B8639224Cd88Ea7 \
    as JSONSchemaValidator5B8639224Cd88Ea7_v1_3_0
from .validators.v1_3_0.jsd_5db21b8e43fab7d8 \
    import JSONSchemaValidator5Db21B8E43FaB7D8 \
    as JSONSchemaValidator5Db21B8E43FaB7D8_v1_3_0
from .validators.v1_3_0.jsd_70ad397649e9b4d3 \
    import JSONSchemaValidator70Ad397649E9B4D3 \
    as JSONSchemaValidator70Ad397649E9B4D3_v1_3_0
from .validators.v1_3_0.jsd_82918a1b4d289c5c \
    import JSONSchemaValidator82918A1B4D289C5C \
    as JSONSchemaValidator82918A1B4D289C5C_v1_3_0
from .validators.v1_3_0.jsd_84b37ae54c59ab28 \
    import JSONSchemaValidator84B37Ae54C59Ab28 \
    as JSONSchemaValidator84B37Ae54C59Ab28_v1_3_0
from .validators.v1_3_0.jsd_81bb4804405a8d2f \
    import JSONSchemaValidator81Bb4804405A8D2F \
    as JSONSchemaValidator81Bb4804405A8D2F_v1_3_0
from .validators.v1_3_0.jsd_84ad8b0e42cab48a \
    import JSONSchemaValidator84Ad8B0E42CaB48A \
    as JSONSchemaValidator84Ad8B0E42CaB48A_v1_3_0
from .validators.v1_3_0.jsd_84b33a9e480abcaf \
    import JSONSchemaValidator84B33A9E480ABcaf \
    as JSONSchemaValidator84B33A9E480ABcaf_v1_3_0
from .validators.v1_3_0.jsd_819f9aa54feab7bf \
    import JSONSchemaValidator819F9Aa54FeaB7Bf \
    as JSONSchemaValidator819F9Aa54FeaB7Bf_v1_3_0
from .validators.v1_3_0.jsd_8fa8eb404a4a8d96 \
    import JSONSchemaValidator8Fa8Eb404A4A8D96 \
    as JSONSchemaValidator8Fa8Eb404A4A8D96_v1_3_0
from .validators.v1_3_0.jsd_ba9dc85b4b8a9a17 \
    import JSONSchemaValidatorBa9DC85B4B8A9A17 \
    as JSONSchemaValidatorBa9DC85B4B8A9A17_v1_3_0
from .validators.v1_3_0.jsd_c9809b6744f8a502 \
    import JSONSchemaValidatorC9809B6744F8A502 \
    as JSONSchemaValidatorC9809B6744F8A502_v1_3_0
from .validators.v1_3_0.jsd_b9855ad54ae98156 \
    import JSONSchemaValidatorB9855Ad54Ae98156 \
    as JSONSchemaValidatorB9855Ad54Ae98156_v1_3_0
from .validators.v1_3_0.jsd_b7bcaa084e2b90d0 \
    import JSONSchemaValidatorB7BcAa084E2B90D0 \
    as JSONSchemaValidatorB7BcAa084E2B90D0_v1_3_0
from .validators.v1_3_0.jsd_cd98780f4888a66d \
    import JSONSchemaValidatorCd98780F4888A66D \
    as JSONSchemaValidatorCd98780F4888A66D_v1_3_0
from .validators.v1_3_0.jsd_cd8469e647caab0e \
    import JSONSchemaValidatorCd8469E647CaAb0E \
    as JSONSchemaValidatorCd8469E647CaAb0E_v1_3_0
from .validators.v1_3_0.jsd_d0a4b88145aabb51 \
    import JSONSchemaValidatorD0A4B88145AaBb51 \
    as JSONSchemaValidatorD0A4B88145AaBb51_v1_3_0
from .validators.v1_3_0.jsd_888f585c49b88441 \
    import JSONSchemaValidator888F585C49B88441 \
    as JSONSchemaValidator888F585C49B88441_v1_3_0
from .validators.v1_3_0.jsd_d888ab6d4d59a8c1 \
    import JSONSchemaValidatorD888Ab6D4D59A8C1 \
    as JSONSchemaValidatorD888Ab6D4D59A8C1_v1_3_0
from .validators.v1_3_0.jsd_f5947a4c439a8bf0 \
    import JSONSchemaValidatorF5947A4C439A8Bf0 \
    as JSONSchemaValidatorF5947A4C439A8Bf0_v1_3_0
from .validators.v1_3_0.jsd_8db939744649a782 \
    import JSONSchemaValidator8Db939744649A782 \
    as JSONSchemaValidator8Db939744649A782_v1_3_0
from .validators.v1_3_0.jsd_eb8249e34f69b0f1 \
    import JSONSchemaValidatorEb8249E34F69B0F1 \
    as JSONSchemaValidatorEb8249E34F69B0F1_v1_3_0
from .validators.v1_3_0.jsd_f6826a8e41bba242 \
    import JSONSchemaValidatorF6826A8E41BbA242 \
    as JSONSchemaValidatorF6826A8E41BbA242_v1_3_0
from .validators.v1_3_0.jsd_aeb9eb67460b92df \
    import JSONSchemaValidatorAeb9Eb67460B92Df \
    as JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_0
from .validators.v1_3_0.jsd_b888792d43baba46 \
    import JSONSchemaValidatorB888792D43BaBa46 \
    as JSONSchemaValidatorB888792D43BaBa46_v1_3_0
from .validators.v1_3_0.jsd_c3b3c9ef4e6b8a09 \
    import JSONSchemaValidatorC3B3C9Ef4E6B8A09 \
    as JSONSchemaValidatorC3B3C9Ef4E6B8A09_v1_3_0
from .validators.v1_3_0.jsd_89b2fb144f5bb09b \
    import JSONSchemaValidator89B2Fb144F5BB09B \
    as JSONSchemaValidator89B2Fb144F5BB09B_v1_3_0
from .validators.v1_3_0.jsd_f49548c54be8a3e2 \
    import JSONSchemaValidatorF49548C54Be8A3E2 \
    as JSONSchemaValidatorF49548C54Be8A3E2_v1_3_0
from .validators.v1_3_0.jsd_ffa748cc44e9a437 \
    import JSONSchemaValidatorFfa748Cc44E9A437 \
    as JSONSchemaValidatorFfa748Cc44E9A437_v1_3_0
from .validators.v1_3_0.jsd_17a82ac94cf99ab0 \
    import JSONSchemaValidator17A82Ac94Cf99Ab0 \
    as JSONSchemaValidator17A82Ac94Cf99Ab0_v1_3_0
from .validators.v1_3_0.jsd_33aab9b842388023 \
    import JSONSchemaValidator33AaB9B842388023 \
    as JSONSchemaValidator33AaB9B842388023_v1_3_0
from .validators.v1_3_0.jsd_23896b124bd8b9bf \
    import JSONSchemaValidator23896B124Bd8B9Bf \
    as JSONSchemaValidator23896B124Bd8B9Bf_v1_3_0
from .validators.v1_3_0.jsd_209509d247599e19 \
    import JSONSchemaValidator209509D247599E19 \
    as JSONSchemaValidator209509D247599E19_v1_3_0
from .validators.v1_3_0.jsd_92acda91406aa050 \
    import JSONSchemaValidator92AcDa91406AA050 \
    as JSONSchemaValidator92AcDa91406AA050_v1_3_0
from .validators.v1_3_0.jsd_d9bdb9034df99dba \
    import JSONSchemaValidatorD9BdB9034Df99Dba \
    as JSONSchemaValidatorD9BdB9034Df99Dba_v1_3_0
from .validators.v1_3_0.jsd_eeb168eb41988e07 \
    import JSONSchemaValidatorEeb168Eb41988E07 \
    as JSONSchemaValidatorEeb168Eb41988E07_v1_3_0
from .validators.v1_3_0.jsd_eba669054e08a60e \
    import JSONSchemaValidatorEba669054E08A60E \
    as JSONSchemaValidatorEba669054E08A60E_v1_3_0
from .validators.v1_3_0.jsd_6284db4649aa8d31 \
    import JSONSchemaValidator6284Db4649Aa8D31 \
    as JSONSchemaValidator6284Db4649Aa8D31_v1_3_0
from .validators.v1_3_0.jsd_9ba14a9e441b8a60 \
    import JSONSchemaValidator9Ba14A9E441B8A60 \
    as JSONSchemaValidator9Ba14A9E441B8A60_v1_3_0
from .validators.v1_3_0.jsd_b2b8cb91459aa58f \
    import JSONSchemaValidatorB2B8Cb91459AA58F \
    as JSONSchemaValidatorB2B8Cb91459AA58F_v1_3_0
from .validators.v1_3_0.jsd_b9b48ac8463a8aba \
    import JSONSchemaValidatorB9B48Ac8463A8Aba \
    as JSONSchemaValidatorB9B48Ac8463A8Aba_v1_3_0
from .validators.v1_3_0.jsd_c2b5fb764d888375 \
    import JSONSchemaValidatorC2B5Fb764D888375 \
    as JSONSchemaValidatorC2B5Fb764D888375_v1_3_0
from .validators.v1_3_0.jsd_ca91da84401abba1 \
    import JSONSchemaValidatorCa91Da84401ABba1 \
    as JSONSchemaValidatorCa91Da84401ABba1_v1_3_0
from .validators.v1_3_0.jsd_149aa93b4ddb80dd \
    import JSONSchemaValidator149AA93B4Ddb80Dd \
    as JSONSchemaValidator149AA93B4Ddb80Dd_v1_3_0
from .validators.v1_3_0.jsd_e2adba7943bab3e9 \
    import JSONSchemaValidatorE2AdBa7943BaB3E9 \
    as JSONSchemaValidatorE2AdBa7943BaB3E9_v1_3_0
from .validators.v1_3_0.jsd_0b836b7b4b6a9fd5 \
    import JSONSchemaValidator0B836B7B4B6A9Fd5 \
    as JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_0
from .validators.v1_3_0.jsd_0a9c988445cb91c8 \
    import JSONSchemaValidator0A9C988445Cb91C8 \
    as JSONSchemaValidator0A9C988445Cb91C8_v1_3_0
from .validators.v1_3_0.jsd_09b0f9ce4239ae10 \
    import JSONSchemaValidator09B0F9Ce4239Ae10 \
    as JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_0
from .validators.v1_3_0.jsd_2499e9ad42e8ae5b \
    import JSONSchemaValidator2499E9Ad42E8Ae5B \
    as JSONSchemaValidator2499E9Ad42E8Ae5B_v1_3_0
from .validators.v1_3_0.jsd_1e962af345b8b59f \
    import JSONSchemaValidator1E962Af345B8B59F \
    as JSONSchemaValidator1E962Af345B8B59F_v1_3_0
from .validators.v1_3_0.jsd_21a6db2540298f55 \
    import JSONSchemaValidator21A6Db2540298F55 \
    as JSONSchemaValidator21A6Db2540298F55_v1_3_0
from .validators.v1_3_0.jsd_3086c9624f498b85 \
    import JSONSchemaValidator3086C9624F498B85 \
    as JSONSchemaValidator3086C9624F498B85_v1_3_0
from .validators.v1_3_0.jsd_3cb24acb486b89d2 \
    import JSONSchemaValidator3Cb24Acb486B89D2 \
    as JSONSchemaValidator3Cb24Acb486B89D2_v1_3_0
from .validators.v1_3_0.jsd_5889fb844939a13b \
    import JSONSchemaValidator5889Fb844939A13B \
    as JSONSchemaValidator5889Fb844939A13B_v1_3_0
from .validators.v1_3_0.jsd_6f9819e84178870c \
    import JSONSchemaValidator6F9819E84178870C \
    as JSONSchemaValidator6F9819E84178870C_v1_3_0
from .validators.v1_3_0.jsd_7989f86846faaf99 \
    import JSONSchemaValidator7989F86846FaAf99 \
    as JSONSchemaValidator7989F86846FaAf99_v1_3_0
from .validators.v1_3_0.jsd_70a479a6462a9496 \
    import JSONSchemaValidator70A479A6462A9496 \
    as JSONSchemaValidator70A479A6462A9496_v1_3_0
from .validators.v1_3_0.jsd_7e92f9eb46db8320 \
    import JSONSchemaValidator7E92F9Eb46Db8320 \
    as JSONSchemaValidator7E92F9Eb46Db8320_v1_3_0
from .validators.v1_3_0.jsd_8da0391947088a5a \
    import JSONSchemaValidator8Da0391947088A5A \
    as JSONSchemaValidator8Da0391947088A5A_v1_3_0
from .validators.v1_3_0.jsd_848b5a7b4f9b8c12 \
    import JSONSchemaValidator848B5A7B4F9B8C12 \
    as JSONSchemaValidator848B5A7B4F9B8C12_v1_3_0
from .validators.v1_3_0.jsd_a4b6c87a4ffb9efa \
    import JSONSchemaValidatorA4B6C87A4Ffb9Efa \
    as JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_0
from .validators.v1_3_0.jsd_9e857b5a4a0bbcdb \
    import JSONSchemaValidator9E857B5A4A0BBcdb \
    as JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_0
from .validators.v1_3_0.jsd_af8d7b0e470b8ae2 \
    import JSONSchemaValidatorAf8D7B0E470B8Ae2 \
    as JSONSchemaValidatorAf8D7B0E470B8Ae2_v1_3_0
from .validators.v1_3_0.jsd_cdab9b474899ae06 \
    import JSONSchemaValidatorCdab9B474899Ae06 \
    as JSONSchemaValidatorCdab9B474899Ae06_v1_3_0
from .validators.v1_3_0.jsd_aeb4dad04a99bbe3 \
    import JSONSchemaValidatorAeb4Dad04A99Bbe3 \
    as JSONSchemaValidatorAeb4Dad04A99Bbe3_v1_3_0
from .validators.v1_3_0.jsd_bab6c9e5440885cc \
    import JSONSchemaValidatorBab6C9E5440885Cc \
    as JSONSchemaValidatorBab6C9E5440885Cc_v1_3_0
from .validators.v1_3_0.jsd_d9a1fa9c4068b23c \
    import JSONSchemaValidatorD9A1Fa9C4068B23C \
    as JSONSchemaValidatorD9A1Fa9C4068B23C_v1_3_0
from .validators.v1_3_0.jsd_80acb88e4ac9ac6d \
    import JSONSchemaValidator80AcB88E4Ac9Ac6D \
    as JSONSchemaValidator80AcB88E4Ac9Ac6D_v1_3_0
from .validators.v1_3_0.jsd_f09319674049a7d4 \
    import JSONSchemaValidatorF09319674049A7D4 \
    as JSONSchemaValidatorF09319674049A7D4_v1_3_0
from .validators.v1_3_0.jsd_e6b3db8046c99654 \
    import JSONSchemaValidatorE6B3Db8046C99654 \
    as JSONSchemaValidatorE6B3Db8046C99654_v1_3_0
from .validators.v1_3_0.jsd_cf9418234d9ab37e \
    import JSONSchemaValidatorCf9418234D9AB37E \
    as JSONSchemaValidatorCf9418234D9AB37E_v1_3_0
from .validators.v1_3_0.jsd_f3b26b5544cabab9 \
    import JSONSchemaValidatorF3B26B5544CaBab9 \
    as JSONSchemaValidatorF3B26B5544CaBab9_v1_3_0
from .validators.v1_3_0.jsd_d8a619974a8a8c48 \
    import JSONSchemaValidatorD8A619974A8A8C48 \
    as JSONSchemaValidatorD8A619974A8A8C48_v1_3_0
from .validators.v1_3_0.jsd_0c8f7a0b49b9aedd \
    import JSONSchemaValidator0C8F7A0B49B9Aedd \
    as JSONSchemaValidator0C8F7A0B49B9Aedd_v1_3_0
from .validators.v1_3_0.jsd_8cb6783b4faba1f4 \
    import JSONSchemaValidator8Cb6783B4FabA1F4 \
    as JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_0
from .validators.v1_3_0.jsd_4dbe3bc743a891bc \
    import JSONSchemaValidator4Dbe3Bc743A891Bc \
    as JSONSchemaValidator4Dbe3Bc743A891Bc_v1_3_0
from .validators.v1_3_0.jsd_fb9beb664f2aba4c \
    import JSONSchemaValidatorFb9BEb664F2ABa4C \
    as JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_0
from .validators.v1_3_0.jsd_bc8aab4746ca883d \
    import JSONSchemaValidatorBc8AAb4746Ca883D \
    as JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_0
from .validators.v1_3_0.jsd_7fbe4b804879baa4 \
    import JSONSchemaValidator7Fbe4B804879Baa4 \
    as JSONSchemaValidator7Fbe4B804879Baa4_v1_3_0
from .validators.v1_3_0.jsd_828828f44f28bd0d \
    import JSONSchemaValidator828828F44F28Bd0D \
    as JSONSchemaValidator828828F44F28Bd0D_v1_3_0
from .validators.v1_3_0.jsd_2f97e8fa45f8b2a3 \
    import JSONSchemaValidator2F97E8Fa45F8B2A3 \
    as JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_0
from .validators.v1_3_0.jsd_ac8ae94c4e69a09d \
    import JSONSchemaValidatorAc8AE94C4E69A09D \
    as JSONSchemaValidatorAc8AE94C4E69A09D_v1_3_0


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


json_schema_validators = {}
json_schema_validators['jsd_01b09a254b9ab259_v1_2_10'] =\
    JSONSchemaValidator01B09A254B9AB259_v1_2_10()
json_schema_validators['jsd_00aec9b1422ab27e_v1_2_10'] =\
    JSONSchemaValidator00AeC9B1422AB27E_v1_2_10()
json_schema_validators['jsd_7781fa0548a98342_v1_2_10'] =\
    JSONSchemaValidator7781Fa0548A98342_v1_2_10()
json_schema_validators['jsd_109d1b4f4289aecd_v1_2_10'] =\
    JSONSchemaValidator109D1B4F4289Aecd_v1_2_10()
json_schema_validators['jsd_6099da82477b858a_v1_2_10'] =\
    JSONSchemaValidator6099Da82477B858A_v1_2_10()
json_schema_validators['jsd_83a3b9404cb88787_v1_2_10'] =\
    JSONSchemaValidator83A3B9404Cb88787_v1_2_10()
json_schema_validators['jsd_9480fa1f47ca9254_v1_2_10'] =\
    JSONSchemaValidator9480Fa1F47Ca9254_v1_2_10()
json_schema_validators['jsd_9c9a785741cbb41f_v1_2_10'] =\
    JSONSchemaValidator9C9A785741CbB41F_v1_2_10()
json_schema_validators['jsd_a7b42836408a8e74_v1_2_10'] =\
    JSONSchemaValidatorA7B42836408A8E74_v1_2_10()
json_schema_validators['jsd_62b05b2c40a9b216_v1_2_10'] =\
    JSONSchemaValidator62B05B2C40A9B216_v1_2_10()
json_schema_validators['jsd_f393abe84989bb48_v1_2_10'] =\
    JSONSchemaValidatorF393Abe84989Bb48_v1_2_10()
json_schema_validators['jsd_d0a1abfa435b841d_v1_2_10'] =\
    JSONSchemaValidatorD0A1Abfa435B841D_v1_2_10()
json_schema_validators['jsd_f6b119ad4d4aaf16_v1_2_10'] =\
    JSONSchemaValidatorF6B119Ad4D4AAf16_v1_2_10()
json_schema_validators['jsd_c8bf6b65414a9bc7_v1_2_10'] =\
    JSONSchemaValidatorC8Bf6B65414A9Bc7_v1_2_10()
json_schema_validators['jsd_00a2fa6146089317_v1_2_10'] =\
    JSONSchemaValidator00A2Fa6146089317_v1_2_10()
json_schema_validators['jsd_2e9db85840fbb1cf_v1_2_10'] =\
    JSONSchemaValidator2E9DB85840FbB1Cf_v1_2_10()
json_schema_validators['jsd_1399891c42a8be64_v1_2_10'] =\
    JSONSchemaValidator1399891C42A8Be64_v1_2_10()
json_schema_validators['jsd_4695090d403b8eaa_v1_2_10'] =\
    JSONSchemaValidator4695090D403B8Eaa_v1_2_10()
json_schema_validators['jsd_45bc7a8344a8bc1e_v1_2_10'] =\
    JSONSchemaValidator45Bc7A8344A8Bc1E_v1_2_10()
json_schema_validators['jsd_4d86a993469a9da9_v1_2_10'] =\
    JSONSchemaValidator4D86A993469A9Da9_v1_2_10()
json_schema_validators['jsd_8091a9b84bfba53b_v1_2_10'] =\
    JSONSchemaValidator8091A9B84BfbA53B_v1_2_10()
json_schema_validators['jsd_429c28154bdaa13d_v1_2_10'] =\
    JSONSchemaValidator429C28154BdaA13D_v1_2_10()
json_schema_validators['jsd_caa3ea704d78b37e_v1_2_10'] =\
    JSONSchemaValidatorCaa3Ea704D78B37E_v1_2_10()
json_schema_validators['jsd_eab7abe048fb99ad_v1_2_10'] =\
    JSONSchemaValidatorEab7Abe048Fb99Ad_v1_2_10()
json_schema_validators['jsd_c1a359b14c89b573_v1_2_10'] =\
    JSONSchemaValidatorC1A359B14C89B573_v1_2_10()
json_schema_validators['jsd_ee9aab01487a8896_v1_2_10'] =\
    JSONSchemaValidatorEe9AAb01487A8896_v1_2_10()
json_schema_validators['jsd_069d9823451b892d_v1_2_10'] =\
    JSONSchemaValidator069D9823451B892D_v1_2_10()
json_schema_validators['jsd_17929bc7465bb564_v1_2_10'] =\
    JSONSchemaValidator17929Bc7465BB564_v1_2_10()
json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_2_10'] =\
    JSONSchemaValidator10B06A6A4F7BB3Cb_v1_2_10()
json_schema_validators['jsd_1da5ebdd434aacfe_v1_2_10'] =\
    JSONSchemaValidator1Da5Ebdd434AAcfe_v1_2_10()
json_schema_validators['jsd_44974ba5435a801d_v1_2_10'] =\
    JSONSchemaValidator44974Ba5435A801D_v1_2_10()
json_schema_validators['jsd_4c8cab5f435a80f4_v1_2_10'] =\
    JSONSchemaValidator4C8CAb5F435A80F4_v1_2_10()
json_schema_validators['jsd_55b439dc4239b140_v1_2_10'] =\
    JSONSchemaValidator55B439Dc4239B140_v1_2_10()
json_schema_validators['jsd_6bacb8d14639bdc7_v1_2_10'] =\
    JSONSchemaValidator6BacB8D14639Bdc7_v1_2_10()
json_schema_validators['jsd_4d9ca8e2431a8a24_v1_2_10'] =\
    JSONSchemaValidator4D9CA8E2431A8A24_v1_2_10()
json_schema_validators['jsd_3d9b99c343398a27_v1_2_10'] =\
    JSONSchemaValidator3D9B99C343398A27_v1_2_10()
json_schema_validators['jsd_709fda3c42b8877a_v1_2_10'] =\
    JSONSchemaValidator709FDa3C42B8877A_v1_2_10()
json_schema_validators['jsd_33b799d04d0a8907_v1_2_10'] =\
    JSONSchemaValidator33B799D04D0A8907_v1_2_10()
json_schema_validators['jsd_7aa3da9d4e098ef2_v1_2_10'] =\
    JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_2_10()
json_schema_validators['jsd_63bb88b74f59aa17_v1_2_10'] =\
    JSONSchemaValidator63Bb88B74F59Aa17_v1_2_10()
json_schema_validators['jsd_9788b8fc4418831d_v1_2_10'] =\
    JSONSchemaValidator9788B8Fc4418831D_v1_2_10()
json_schema_validators['jsd_948ea8194348bc0b_v1_2_10'] =\
    JSONSchemaValidator948EA8194348Bc0B_v1_2_10()
json_schema_validators['jsd_47a1b84b4e1b8044_v1_2_10'] =\
    JSONSchemaValidator47A1B84B4E1B8044_v1_2_10()
json_schema_validators['jsd_99872a134d0a9fb4_v1_2_10'] =\
    JSONSchemaValidator99872A134D0A9Fb4_v1_2_10()
json_schema_validators['jsd_a5ac99774c6bb541_v1_2_10'] =\
    JSONSchemaValidatorA5Ac99774C6BB541_v1_2_10()
json_schema_validators['jsd_a4967be64dfaaa1a_v1_2_10'] =\
    JSONSchemaValidatorA4967Be64DfaAa1A_v1_2_10()
json_schema_validators['jsd_a6b798ab4acaa34e_v1_2_10'] =\
    JSONSchemaValidatorA6B798Ab4AcaA34E_v1_2_10()
json_schema_validators['jsd_58a3699e489b9529_v1_2_10'] =\
    JSONSchemaValidator58A3699E489B9529_v1_2_10()
json_schema_validators['jsd_b68a6bd8473a9a25_v1_2_10'] =\
    JSONSchemaValidatorB68A6Bd8473A9A25_v1_2_10()
json_schema_validators['jsd_c1ba9a424c08a01b_v1_2_10'] =\
    JSONSchemaValidatorC1Ba9A424C08A01B_v1_2_10()
json_schema_validators['jsd_bf859ac64a0ba19c_v1_2_10'] =\
    JSONSchemaValidatorBf859Ac64A0BA19C_v1_2_10()
json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_2_10'] =\
    JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_2_10()
json_schema_validators['jsd_db8e09234a988bab_v1_2_10'] =\
    JSONSchemaValidatorDb8E09234A988Bab_v1_2_10()
json_schema_validators['jsd_f5ac590c4ca9975a_v1_2_10'] =\
    JSONSchemaValidatorF5Ac590C4Ca9975A_v1_2_10()
json_schema_validators['jsd_89b36b4649999d81_v1_2_10'] =\
    JSONSchemaValidator89B36B4649999D81_v1_2_10()
json_schema_validators['jsd_fba0d80747eb82e8_v1_2_10'] =\
    JSONSchemaValidatorFba0D80747Eb82E8_v1_2_10()
json_schema_validators['jsd_979688084b7ba60d_v1_2_10'] =\
    JSONSchemaValidator979688084B7BA60D_v1_2_10()
json_schema_validators['jsd_a6965b454c9a8663_v1_2_10'] =\
    JSONSchemaValidatorA6965B454C9A8663_v1_2_10()
json_schema_validators['jsd_f6ac994f451ba011_v1_2_10'] =\
    JSONSchemaValidatorF6Ac994F451BA011_v1_2_10()
json_schema_validators['jsd_ff816b8e435897eb_v1_2_10'] =\
    JSONSchemaValidatorFf816B8E435897Eb_v1_2_10()
json_schema_validators['jsd_26b44ab04649a183_v1_2_10'] =\
    JSONSchemaValidator26B44Ab04649A183_v1_2_10()
json_schema_validators['jsd_a1a9387346ba92b1_v1_2_10'] =\
    JSONSchemaValidatorA1A9387346Ba92B1_v1_2_10()
json_schema_validators['jsd_e78bb8a2449b9eed_v1_2_10'] =\
    JSONSchemaValidatorE78BB8A2449B9Eed_v1_2_10()
json_schema_validators['jsd_f5a269c44f2a95fa_v1_2_10'] =\
    JSONSchemaValidatorF5A269C44F2A95Fa_v1_2_10()
json_schema_validators['jsd_e487f8d3481b94f2_v1_2_10'] =\
    JSONSchemaValidatorE487F8D3481B94F2_v1_2_10()
json_schema_validators['jsd_33bb2b9d40199e14_v1_2_10'] =\
    JSONSchemaValidator33Bb2B9D40199E14_v1_2_10()
json_schema_validators['jsd_d6b8ca774739adf4_v1_2_10'] =\
    JSONSchemaValidatorD6B8Ca774739Adf4_v1_2_10()
json_schema_validators['jsd_3f89bbfc4f6b8b50_v1_2_10'] =\
    JSONSchemaValidator3F89Bbfc4F6B8B50_v1_2_10()
json_schema_validators['jsd_42b6a86e44b8bdfc_v1_2_10'] =\
    JSONSchemaValidator42B6A86E44B8Bdfc_v1_2_10()
json_schema_validators['jsd_9698c8ec4a0b8c1a_v1_2_10'] =\
    JSONSchemaValidator9698C8Ec4A0B8C1A_v1_2_10()
json_schema_validators['jsd_55bc3bf94e38b6ff_v1_2_10'] =\
    JSONSchemaValidator55Bc3Bf94E38B6Ff_v1_2_10()
json_schema_validators['jsd_8a9d2b76443b914e_v1_2_10'] =\
    JSONSchemaValidator8A9D2B76443B914E_v1_2_10()
json_schema_validators['jsd_a395fae644ca899c_v1_2_10'] =\
    JSONSchemaValidatorA395Fae644Ca899C_v1_2_10()
json_schema_validators['jsd_7ab9a8bd4f3b86a4_v1_2_10'] =\
    JSONSchemaValidator7Ab9A8Bd4F3B86A4_v1_2_10()
json_schema_validators['jsd_0c8f7a0b49b9aedd_v1_2_10'] =\
    JSONSchemaValidator0C8F7A0B49B9Aedd_v1_2_10()
json_schema_validators['jsd_8cb6783b4faba1f4_v1_2_10'] =\
    JSONSchemaValidator8Cb6783B4FabA1F4_v1_2_10()
json_schema_validators['jsd_4dbe3bc743a891bc_v1_2_10'] =\
    JSONSchemaValidator4Dbe3Bc743A891Bc_v1_2_10()
json_schema_validators['jsd_bc8aab4746ca883d_v1_2_10'] =\
    JSONSchemaValidatorBc8AAb4746Ca883D_v1_2_10()
json_schema_validators['jsd_fb9beb664f2aba4c_v1_2_10'] =\
    JSONSchemaValidatorFb9BEb664F2ABa4C_v1_2_10()
json_schema_validators['jsd_0a9c988445cb91c8_v1_2_10'] =\
    JSONSchemaValidator0A9C988445Cb91C8_v1_2_10()
json_schema_validators['jsd_21a6db2540298f55_v1_2_10'] =\
    JSONSchemaValidator21A6Db2540298F55_v1_2_10()
json_schema_validators['jsd_3086c9624f498b85_v1_2_10'] =\
    JSONSchemaValidator3086C9624F498B85_v1_2_10()
json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_2_10'] =\
    JSONSchemaValidator0B836B7B4B6A9Fd5_v1_2_10()
json_schema_validators['jsd_1e962af345b8b59f_v1_2_10'] =\
    JSONSchemaValidator1E962Af345B8B59F_v1_2_10()
json_schema_validators['jsd_09b0f9ce4239ae10_v1_2_10'] =\
    JSONSchemaValidator09B0F9Ce4239Ae10_v1_2_10()
json_schema_validators['jsd_5889fb844939a13b_v1_2_10'] =\
    JSONSchemaValidator5889Fb844939A13B_v1_2_10()
json_schema_validators['jsd_2499e9ad42e8ae5b_v1_2_10'] =\
    JSONSchemaValidator2499E9Ad42E8Ae5B_v1_2_10()
json_schema_validators['jsd_3cb24acb486b89d2_v1_2_10'] =\
    JSONSchemaValidator3Cb24Acb486B89D2_v1_2_10()
json_schema_validators['jsd_80acb88e4ac9ac6d_v1_2_10'] =\
    JSONSchemaValidator80AcB88E4Ac9Ac6D_v1_2_10()
json_schema_validators['jsd_6f9819e84178870c_v1_2_10'] =\
    JSONSchemaValidator6F9819E84178870C_v1_2_10()
json_schema_validators['jsd_7989f86846faaf99_v1_2_10'] =\
    JSONSchemaValidator7989F86846FaAf99_v1_2_10()
json_schema_validators['jsd_8da0391947088a5a_v1_2_10'] =\
    JSONSchemaValidator8Da0391947088A5A_v1_2_10()
json_schema_validators['jsd_7e92f9eb46db8320_v1_2_10'] =\
    JSONSchemaValidator7E92F9Eb46Db8320_v1_2_10()
json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_2_10'] =\
    JSONSchemaValidator9E857B5A4A0BBcdb_v1_2_10()
json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_2_10'] =\
    JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_2_10()
json_schema_validators['jsd_aeb4dad04a99bbe3_v1_2_10'] =\
    JSONSchemaValidatorAeb4Dad04A99Bbe3_v1_2_10()
json_schema_validators['jsd_af8d7b0e470b8ae2_v1_2_10'] =\
    JSONSchemaValidatorAf8D7B0E470B8Ae2_v1_2_10()
json_schema_validators['jsd_bab6c9e5440885cc_v1_2_10'] =\
    JSONSchemaValidatorBab6C9E5440885Cc_v1_2_10()
json_schema_validators['jsd_70a479a6462a9496_v1_2_10'] =\
    JSONSchemaValidator70A479A6462A9496_v1_2_10()
json_schema_validators['jsd_cf9418234d9ab37e_v1_2_10'] =\
    JSONSchemaValidatorCf9418234D9AB37E_v1_2_10()
json_schema_validators['jsd_d8a619974a8a8c48_v1_2_10'] =\
    JSONSchemaValidatorD8A619974A8A8C48_v1_2_10()
json_schema_validators['jsd_e6b3db8046c99654_v1_2_10'] =\
    JSONSchemaValidatorE6B3Db8046C99654_v1_2_10()
json_schema_validators['jsd_848b5a7b4f9b8c12_v1_2_10'] =\
    JSONSchemaValidator848B5A7B4F9B8C12_v1_2_10()
json_schema_validators['jsd_d9a1fa9c4068b23c_v1_2_10'] =\
    JSONSchemaValidatorD9A1Fa9C4068B23C_v1_2_10()
json_schema_validators['jsd_f09319674049a7d4_v1_2_10'] =\
    JSONSchemaValidatorF09319674049A7D4_v1_2_10()
json_schema_validators['jsd_cdab9b474899ae06_v1_2_10'] =\
    JSONSchemaValidatorCdab9B474899Ae06_v1_2_10()
json_schema_validators['jsd_f3b26b5544cabab9_v1_2_10'] =\
    JSONSchemaValidatorF3B26B5544CaBab9_v1_2_10()
json_schema_validators['jsd_7fbe4b804879baa4_v1_2_10'] =\
    JSONSchemaValidator7Fbe4B804879Baa4_v1_2_10()
json_schema_validators['jsd_828828f44f28bd0d_v1_2_10'] =\
    JSONSchemaValidator828828F44F28Bd0D_v1_2_10()
json_schema_validators['jsd_0db7da744c0b83d8_v1_2_10'] =\
    JSONSchemaValidator0Db7Da744C0B83D8_v1_2_10()
json_schema_validators['jsd_3d923b184dc9a4ca_v1_2_10'] =\
    JSONSchemaValidator3D923B184Dc9A4Ca_v1_2_10()
json_schema_validators['jsd_3b9ef9674429be4c_v1_2_10'] =\
    JSONSchemaValidator3B9EF9674429Be4C_v1_2_10()
json_schema_validators['jsd_20b19b52464b8972_v1_2_10'] =\
    JSONSchemaValidator20B19B52464B8972_v1_2_10()
json_schema_validators['jsd_38bd0b884b89a785_v1_2_10'] =\
    JSONSchemaValidator38Bd0B884B89A785_v1_2_10()
json_schema_validators['jsd_5db21b8e43fab7d8_v1_2_10'] =\
    JSONSchemaValidator5Db21B8E43FaB7D8_v1_2_10()
json_schema_validators['jsd_288df9494f2a9746_v1_2_10'] =\
    JSONSchemaValidator288DF9494F2A9746_v1_2_10()
json_schema_validators['jsd_349c888443b89a58_v1_2_10'] =\
    JSONSchemaValidator349C888443B89A58_v1_2_10()
json_schema_validators['jsd_1c894b5848eab214_v1_2_10'] =\
    JSONSchemaValidator1C894B5848EaB214_v1_2_10()
json_schema_validators['jsd_84b33a9e480abcaf_v1_2_10'] =\
    JSONSchemaValidator84B33A9E480ABcaf_v1_2_10()
json_schema_validators['jsd_4bb22af046fa8f08_v1_2_10'] =\
    JSONSchemaValidator4Bb22Af046Fa8F08_v1_2_10()
json_schema_validators['jsd_888f585c49b88441_v1_2_10'] =\
    JSONSchemaValidator888F585C49B88441_v1_2_10()
json_schema_validators['jsd_4eb56a614cc9a2d2_v1_2_10'] =\
    JSONSchemaValidator4Eb56A614Cc9A2D2_v1_2_10()
json_schema_validators['jsd_82918a1b4d289c5c_v1_2_10'] =\
    JSONSchemaValidator82918A1B4D289C5C_v1_2_10()
json_schema_validators['jsd_8db939744649a782_v1_2_10'] =\
    JSONSchemaValidator8Db939744649A782_v1_2_10()
json_schema_validators['jsd_5b8639224cd88ea7_v1_2_10'] =\
    JSONSchemaValidator5B8639224Cd88Ea7_v1_2_10()
json_schema_validators['jsd_84b37ae54c59ab28_v1_2_10'] =\
    JSONSchemaValidator84B37Ae54C59Ab28_v1_2_10()
json_schema_validators['jsd_70ad397649e9b4d3_v1_2_10'] =\
    JSONSchemaValidator70Ad397649E9B4D3_v1_2_10()
json_schema_validators['jsd_81bb4804405a8d2f_v1_2_10'] =\
    JSONSchemaValidator81Bb4804405A8D2F_v1_2_10()
json_schema_validators['jsd_84ad8b0e42cab48a_v1_2_10'] =\
    JSONSchemaValidator84Ad8B0E42CaB48A_v1_2_10()
json_schema_validators['jsd_b7bcaa084e2b90d0_v1_2_10'] =\
    JSONSchemaValidatorB7BcAa084E2B90D0_v1_2_10()
json_schema_validators['jsd_b9855ad54ae98156_v1_2_10'] =\
    JSONSchemaValidatorB9855Ad54Ae98156_v1_2_10()
json_schema_validators['jsd_ba9dc85b4b8a9a17_v1_2_10'] =\
    JSONSchemaValidatorBa9DC85B4B8A9A17_v1_2_10()
json_schema_validators['jsd_cd8469e647caab0e_v1_2_10'] =\
    JSONSchemaValidatorCd8469E647CaAb0E_v1_2_10()
json_schema_validators['jsd_d0a4b88145aabb51_v1_2_10'] =\
    JSONSchemaValidatorD0A4B88145AaBb51_v1_2_10()
json_schema_validators['jsd_819f9aa54feab7bf_v1_2_10'] =\
    JSONSchemaValidator819F9Aa54FeaB7Bf_v1_2_10()
json_schema_validators['jsd_8fa8eb404a4a8d96_v1_2_10'] =\
    JSONSchemaValidator8Fa8Eb404A4A8D96_v1_2_10()
json_schema_validators['jsd_f5947a4c439a8bf0_v1_2_10'] =\
    JSONSchemaValidatorF5947A4C439A8Bf0_v1_2_10()
json_schema_validators['jsd_aeb9eb67460b92df_v1_2_10'] =\
    JSONSchemaValidatorAeb9Eb67460B92Df_v1_2_10()
json_schema_validators['jsd_b888792d43baba46_v1_2_10'] =\
    JSONSchemaValidatorB888792D43BaBa46_v1_2_10()
json_schema_validators['jsd_c3b3c9ef4e6b8a09_v1_2_10'] =\
    JSONSchemaValidatorC3B3C9Ef4E6B8A09_v1_2_10()
json_schema_validators['jsd_c9809b6744f8a502_v1_2_10'] =\
    JSONSchemaValidatorC9809B6744F8A502_v1_2_10()
json_schema_validators['jsd_d888ab6d4d59a8c1_v1_2_10'] =\
    JSONSchemaValidatorD888Ab6D4D59A8C1_v1_2_10()
json_schema_validators['jsd_cd98780f4888a66d_v1_2_10'] =\
    JSONSchemaValidatorCd98780F4888A66D_v1_2_10()
json_schema_validators['jsd_f49548c54be8a3e2_v1_2_10'] =\
    JSONSchemaValidatorF49548C54Be8A3E2_v1_2_10()
json_schema_validators['jsd_ffa748cc44e9a437_v1_2_10'] =\
    JSONSchemaValidatorFfa748Cc44E9A437_v1_2_10()
json_schema_validators['jsd_eb8249e34f69b0f1_v1_2_10'] =\
    JSONSchemaValidatorEb8249E34F69B0F1_v1_2_10()
json_schema_validators['jsd_f6826a8e41bba242_v1_2_10'] =\
    JSONSchemaValidatorF6826A8E41BbA242_v1_2_10()
json_schema_validators['jsd_89b2fb144f5bb09b_v1_2_10'] =\
    JSONSchemaValidator89B2Fb144F5BB09B_v1_2_10()
json_schema_validators['jsd_17a82ac94cf99ab0_v1_2_10'] =\
    JSONSchemaValidator17A82Ac94Cf99Ab0_v1_2_10()
json_schema_validators['jsd_eeb168eb41988e07_v1_2_10'] =\
    JSONSchemaValidatorEeb168Eb41988E07_v1_2_10()
json_schema_validators['jsd_50b589fd4c7a930a_v1_2_10'] =\
    JSONSchemaValidator50B589Fd4C7A930A_v1_2_10()
json_schema_validators['jsd_6284db4649aa8d31_v1_2_10'] =\
    JSONSchemaValidator6284Db4649Aa8D31_v1_2_10()
json_schema_validators['jsd_9ba14a9e441b8a60_v1_2_10'] =\
    JSONSchemaValidator9Ba14A9E441B8A60_v1_2_10()
json_schema_validators['jsd_b2b8cb91459aa58f_v1_2_10'] =\
    JSONSchemaValidatorB2B8Cb91459AA58F_v1_2_10()
json_schema_validators['jsd_c2b5fb764d888375_v1_2_10'] =\
    JSONSchemaValidatorC2B5Fb764D888375_v1_2_10()
json_schema_validators['jsd_b9b48ac8463a8aba_v1_2_10'] =\
    JSONSchemaValidatorB9B48Ac8463A8Aba_v1_2_10()
json_schema_validators['jsd_ca91da84401abba1_v1_2_10'] =\
    JSONSchemaValidatorCa91Da84401ABba1_v1_2_10()
json_schema_validators['jsd_149aa93b4ddb80dd_v1_2_10'] =\
    JSONSchemaValidator149AA93B4Ddb80Dd_v1_2_10()
json_schema_validators['jsd_e2adba7943bab3e9_v1_2_10'] =\
    JSONSchemaValidatorE2AdBa7943BaB3E9_v1_2_10()
json_schema_validators['jsd_ac8ae94c4e69a09d_v1_2_10'] =\
    JSONSchemaValidatorAc8AE94C4E69A09D_v1_2_10()
json_schema_validators['jsd_cca098344a489dfa_v1_2_10'] =\
    JSONSchemaValidatorCca098344A489Dfa_v1_2_10()
json_schema_validators['jsd_8a96fb954d09a349_v1_2_10'] =\
    JSONSchemaValidator8A96Fb954D09A349_v1_2_10()
json_schema_validators['jsd_db9f997f4e59aec1_v1_2_10'] =\
    JSONSchemaValidatorDb9F997F4E59Aec1_v1_2_10()
json_schema_validators['jsd_c7a6592b4b98a369_v1_2_10'] =\
    JSONSchemaValidatorC7A6592B4B98A369_v1_2_10()
json_schema_validators['jsd_cca519ba45ebb423_v1_2_10'] =\
    JSONSchemaValidatorCca519Ba45EbB423_v1_2_10()
json_schema_validators['jsd_98a39bf4485a9871_v1_2_10'] =\
    JSONSchemaValidator98A39Bf4485A9871_v1_2_10()
json_schema_validators['jsd_bead7b3443b996a7_v1_2_10'] =\
    JSONSchemaValidatorBead7B3443B996A7_v1_2_10()
json_schema_validators['jsd_cb81b93540baaab0_v1_2_10'] =\
    JSONSchemaValidatorCb81B93540BaAab0_v1_2_10()
json_schema_validators['jsd_00aec9b1422ab27e_v1_3_0'] =\
    JSONSchemaValidator00AeC9B1422AB27E_v1_3_0()
json_schema_validators['jsd_01b09a254b9ab259_v1_3_0'] =\
    JSONSchemaValidator01B09A254B9AB259_v1_3_0()
json_schema_validators['jsd_109d1b4f4289aecd_v1_3_0'] =\
    JSONSchemaValidator109D1B4F4289Aecd_v1_3_0()
json_schema_validators['jsd_6099da82477b858a_v1_3_0'] =\
    JSONSchemaValidator6099Da82477B858A_v1_3_0()
json_schema_validators['jsd_7781fa0548a98342_v1_3_0'] =\
    JSONSchemaValidator7781Fa0548A98342_v1_3_0()
json_schema_validators['jsd_9480fa1f47ca9254_v1_3_0'] =\
    JSONSchemaValidator9480Fa1F47Ca9254_v1_3_0()
json_schema_validators['jsd_a7b42836408a8e74_v1_3_0'] =\
    JSONSchemaValidatorA7B42836408A8E74_v1_3_0()
json_schema_validators['jsd_f393abe84989bb48_v1_3_0'] =\
    JSONSchemaValidatorF393Abe84989Bb48_v1_3_0()
json_schema_validators['jsd_c8bf6b65414a9bc7_v1_3_0'] =\
    JSONSchemaValidatorC8Bf6B65414A9Bc7_v1_3_0()
json_schema_validators['jsd_62b05b2c40a9b216_v1_3_0'] =\
    JSONSchemaValidator62B05B2C40A9B216_v1_3_0()
json_schema_validators['jsd_83a3b9404cb88787_v1_3_0'] =\
    JSONSchemaValidator83A3B9404Cb88787_v1_3_0()
json_schema_validators['jsd_f6b119ad4d4aaf16_v1_3_0'] =\
    JSONSchemaValidatorF6B119Ad4D4AAf16_v1_3_0()
json_schema_validators['jsd_9c9a785741cbb41f_v1_3_0'] =\
    JSONSchemaValidator9C9A785741CbB41F_v1_3_0()
json_schema_validators['jsd_d0a1abfa435b841d_v1_3_0'] =\
    JSONSchemaValidatorD0A1Abfa435B841D_v1_3_0()
json_schema_validators['jsd_00a2fa6146089317_v1_3_0'] =\
    JSONSchemaValidator00A2Fa6146089317_v1_3_0()
json_schema_validators['jsd_1399891c42a8be64_v1_3_0'] =\
    JSONSchemaValidator1399891C42A8Be64_v1_3_0()
json_schema_validators['jsd_429c28154bdaa13d_v1_3_0'] =\
    JSONSchemaValidator429C28154BdaA13D_v1_3_0()
json_schema_validators['jsd_2e9db85840fbb1cf_v1_3_0'] =\
    JSONSchemaValidator2E9DB85840FbB1Cf_v1_3_0()
json_schema_validators['jsd_4695090d403b8eaa_v1_3_0'] =\
    JSONSchemaValidator4695090D403B8Eaa_v1_3_0()
json_schema_validators['jsd_45bc7a8344a8bc1e_v1_3_0'] =\
    JSONSchemaValidator45Bc7A8344A8Bc1E_v1_3_0()
json_schema_validators['jsd_4d86a993469a9da9_v1_3_0'] =\
    JSONSchemaValidator4D86A993469A9Da9_v1_3_0()
json_schema_validators['jsd_8091a9b84bfba53b_v1_3_0'] =\
    JSONSchemaValidator8091A9B84BfbA53B_v1_3_0()
json_schema_validators['jsd_c1a359b14c89b573_v1_3_0'] =\
    JSONSchemaValidatorC1A359B14C89B573_v1_3_0()
json_schema_validators['jsd_eab7abe048fb99ad_v1_3_0'] =\
    JSONSchemaValidatorEab7Abe048Fb99Ad_v1_3_0()
json_schema_validators['jsd_caa3ea704d78b37e_v1_3_0'] =\
    JSONSchemaValidatorCaa3Ea704D78B37E_v1_3_0()
json_schema_validators['jsd_ee9aab01487a8896_v1_3_0'] =\
    JSONSchemaValidatorEe9AAb01487A8896_v1_3_0()
json_schema_validators['jsd_069d9823451b892d_v1_3_0'] =\
    JSONSchemaValidator069D9823451B892D_v1_3_0()
json_schema_validators['jsd_17929bc7465bb564_v1_3_0'] =\
    JSONSchemaValidator17929Bc7465BB564_v1_3_0()
json_schema_validators['jsd_10b06a6a4f7bb3cb_v1_3_0'] =\
    JSONSchemaValidator10B06A6A4F7BB3Cb_v1_3_0()
json_schema_validators['jsd_1da5ebdd434aacfe_v1_3_0'] =\
    JSONSchemaValidator1Da5Ebdd434AAcfe_v1_3_0()
json_schema_validators['jsd_47a1b84b4e1b8044_v1_3_0'] =\
    JSONSchemaValidator47A1B84B4E1B8044_v1_3_0()
json_schema_validators['jsd_33b799d04d0a8907_v1_3_0'] =\
    JSONSchemaValidator33B799D04D0A8907_v1_3_0()
json_schema_validators['jsd_3d9b99c343398a27_v1_3_0'] =\
    JSONSchemaValidator3D9B99C343398A27_v1_3_0()
json_schema_validators['jsd_4d9ca8e2431a8a24_v1_3_0'] =\
    JSONSchemaValidator4D9CA8E2431A8A24_v1_3_0()
json_schema_validators['jsd_44974ba5435a801d_v1_3_0'] =\
    JSONSchemaValidator44974Ba5435A801D_v1_3_0()
json_schema_validators['jsd_4c8cab5f435a80f4_v1_3_0'] =\
    JSONSchemaValidator4C8CAb5F435A80F4_v1_3_0()
json_schema_validators['jsd_55b439dc4239b140_v1_3_0'] =\
    JSONSchemaValidator55B439Dc4239B140_v1_3_0()
json_schema_validators['jsd_63bb88b74f59aa17_v1_3_0'] =\
    JSONSchemaValidator63Bb88B74F59Aa17_v1_3_0()
json_schema_validators['jsd_6bacb8d14639bdc7_v1_3_0'] =\
    JSONSchemaValidator6BacB8D14639Bdc7_v1_3_0()
json_schema_validators['jsd_948ea8194348bc0b_v1_3_0'] =\
    JSONSchemaValidator948EA8194348Bc0B_v1_3_0()
json_schema_validators['jsd_89b36b4649999d81_v1_3_0'] =\
    JSONSchemaValidator89B36B4649999D81_v1_3_0()
json_schema_validators['jsd_99872a134d0a9fb4_v1_3_0'] =\
    JSONSchemaValidator99872A134D0A9Fb4_v1_3_0()
json_schema_validators['jsd_979688084b7ba60d_v1_3_0'] =\
    JSONSchemaValidator979688084B7BA60D_v1_3_0()
json_schema_validators['jsd_a5ac99774c6bb541_v1_3_0'] =\
    JSONSchemaValidatorA5Ac99774C6BB541_v1_3_0()
json_schema_validators['jsd_9788b8fc4418831d_v1_3_0'] =\
    JSONSchemaValidator9788B8Fc4418831D_v1_3_0()
json_schema_validators['jsd_b68a6bd8473a9a25_v1_3_0'] =\
    JSONSchemaValidatorB68A6Bd8473A9A25_v1_3_0()
json_schema_validators['jsd_c1ba9a424c08a01b_v1_3_0'] =\
    JSONSchemaValidatorC1Ba9A424C08A01B_v1_3_0()
json_schema_validators['jsd_db8e09234a988bab_v1_3_0'] =\
    JSONSchemaValidatorDb8E09234A988Bab_v1_3_0()
json_schema_validators['jsd_a6965b454c9a8663_v1_3_0'] =\
    JSONSchemaValidatorA6965B454C9A8663_v1_3_0()
json_schema_validators['jsd_f5ac590c4ca9975a_v1_3_0'] =\
    JSONSchemaValidatorF5Ac590C4Ca9975A_v1_3_0()
json_schema_validators['jsd_fba0d80747eb82e8_v1_3_0'] =\
    JSONSchemaValidatorFba0D80747Eb82E8_v1_3_0()
json_schema_validators['jsd_bf859ac64a0ba19c_v1_3_0'] =\
    JSONSchemaValidatorBf859Ac64A0BA19C_v1_3_0()
json_schema_validators['jsd_c5acd9fa4c1a8abc_v1_3_0'] =\
    JSONSchemaValidatorC5AcD9Fa4C1A8Abc_v1_3_0()
json_schema_validators['jsd_58a3699e489b9529_v1_3_0'] =\
    JSONSchemaValidator58A3699E489B9529_v1_3_0()
json_schema_validators['jsd_709fda3c42b8877a_v1_3_0'] =\
    JSONSchemaValidator709FDa3C42B8877A_v1_3_0()
json_schema_validators['jsd_7aa3da9d4e098ef2_v1_3_0'] =\
    JSONSchemaValidator7Aa3Da9D4E098Ef2_v1_3_0()
json_schema_validators['jsd_a4967be64dfaaa1a_v1_3_0'] =\
    JSONSchemaValidatorA4967Be64DfaAa1A_v1_3_0()
json_schema_validators['jsd_a6b798ab4acaa34e_v1_3_0'] =\
    JSONSchemaValidatorA6B798Ab4AcaA34E_v1_3_0()
json_schema_validators['jsd_ff816b8e435897eb_v1_3_0'] =\
    JSONSchemaValidatorFf816B8E435897Eb_v1_3_0()
json_schema_validators['jsd_f6ac994f451ba011_v1_3_0'] =\
    JSONSchemaValidatorF6Ac994F451BA011_v1_3_0()
json_schema_validators['jsd_26b44ab04649a183_v1_3_0'] =\
    JSONSchemaValidator26B44Ab04649A183_v1_3_0()
json_schema_validators['jsd_a1a9387346ba92b1_v1_3_0'] =\
    JSONSchemaValidatorA1A9387346Ba92B1_v1_3_0()
json_schema_validators['jsd_e78bb8a2449b9eed_v1_3_0'] =\
    JSONSchemaValidatorE78BB8A2449B9Eed_v1_3_0()
json_schema_validators['jsd_f5a269c44f2a95fa_v1_3_0'] =\
    JSONSchemaValidatorF5A269C44F2A95Fa_v1_3_0()
json_schema_validators['jsd_e487f8d3481b94f2_v1_3_0'] =\
    JSONSchemaValidatorE487F8D3481B94F2_v1_3_0()
json_schema_validators['jsd_33bb2b9d40199e14_v1_3_0'] =\
    JSONSchemaValidator33Bb2B9D40199E14_v1_3_0()
json_schema_validators['jsd_d6b8ca774739adf4_v1_3_0'] =\
    JSONSchemaValidatorD6B8Ca774739Adf4_v1_3_0()
json_schema_validators['jsd_3f89bbfc4f6b8b50_v1_3_0'] =\
    JSONSchemaValidator3F89Bbfc4F6B8B50_v1_3_0()
json_schema_validators['jsd_42b6a86e44b8bdfc_v1_3_0'] =\
    JSONSchemaValidator42B6A86E44B8Bdfc_v1_3_0()
json_schema_validators['jsd_9698c8ec4a0b8c1a_v1_3_0'] =\
    JSONSchemaValidator9698C8Ec4A0B8C1A_v1_3_0()
json_schema_validators['jsd_55bc3bf94e38b6ff_v1_3_0'] =\
    JSONSchemaValidator55Bc3Bf94E38B6Ff_v1_3_0()
json_schema_validators['jsd_7ab9a8bd4f3b86a4_v1_3_0'] =\
    JSONSchemaValidator7Ab9A8Bd4F3B86A4_v1_3_0()
json_schema_validators['jsd_8a9d2b76443b914e_v1_3_0'] =\
    JSONSchemaValidator8A9D2B76443B914E_v1_3_0()
json_schema_validators['jsd_a395fae644ca899c_v1_3_0'] =\
    JSONSchemaValidatorA395Fae644Ca899C_v1_3_0()
json_schema_validators['jsd_07913b7f4e1880de_v1_3_0'] =\
    JSONSchemaValidator07913B7F4E1880De_v1_3_0()
json_schema_validators['jsd_20872aec43b9bf50_v1_3_0'] =\
    JSONSchemaValidator20872Aec43B9Bf50_v1_3_0()
json_schema_validators['jsd_6896993e41b8bd7a_v1_3_0'] =\
    JSONSchemaValidator6896993E41B8Bd7A_v1_3_0()
json_schema_validators['jsd_a0be3a2f47ab9f3c_v1_3_0'] =\
    JSONSchemaValidatorA0Be3A2F47Ab9F3C_v1_3_0()
json_schema_validators['jsd_ae86a8c14b5980b7_v1_3_0'] =\
    JSONSchemaValidatorAe86A8C14B5980B7_v1_3_0()
json_schema_validators['jsd_47ba59204e0ab742_v1_3_0'] =\
    JSONSchemaValidator47Ba59204E0AB742_v1_3_0()
json_schema_validators['jsd_db9f997f4e59aec1_v1_3_0'] =\
    JSONSchemaValidatorDb9F997F4E59Aec1_v1_3_0()
json_schema_validators['jsd_c7a6592b4b98a369_v1_3_0'] =\
    JSONSchemaValidatorC7A6592B4B98A369_v1_3_0()
json_schema_validators['jsd_cca098344a489dfa_v1_3_0'] =\
    JSONSchemaValidatorCca098344A489Dfa_v1_3_0()
json_schema_validators['jsd_cca519ba45ebb423_v1_3_0'] =\
    JSONSchemaValidatorCca519Ba45EbB423_v1_3_0()
json_schema_validators['jsd_8a96fb954d09a349_v1_3_0'] =\
    JSONSchemaValidator8A96Fb954D09A349_v1_3_0()
json_schema_validators['jsd_1e80bb50430b8634_v1_3_0'] =\
    JSONSchemaValidator1E80Bb50430B8634_v1_3_0()
json_schema_validators['jsd_a4b56a5f478a97dd_v1_3_0'] =\
    JSONSchemaValidatorA4B56A5F478A97Dd_v1_3_0()
json_schema_validators['jsd_d0b3593c4a7aaf22_v1_3_0'] =\
    JSONSchemaValidatorD0B3593C4A7AAf22_v1_3_0()
json_schema_validators['jsd_0db7da744c0b83d8_v1_3_0'] =\
    JSONSchemaValidator0Db7Da744C0B83D8_v1_3_0()
json_schema_validators['jsd_1c894b5848eab214_v1_3_0'] =\
    JSONSchemaValidator1C894B5848EaB214_v1_3_0()
json_schema_validators['jsd_3b9ef9674429be4c_v1_3_0'] =\
    JSONSchemaValidator3B9EF9674429Be4C_v1_3_0()
json_schema_validators['jsd_20b19b52464b8972_v1_3_0'] =\
    JSONSchemaValidator20B19B52464B8972_v1_3_0()
json_schema_validators['jsd_288df9494f2a9746_v1_3_0'] =\
    JSONSchemaValidator288DF9494F2A9746_v1_3_0()
json_schema_validators['jsd_38bd0b884b89a785_v1_3_0'] =\
    JSONSchemaValidator38Bd0B884B89A785_v1_3_0()
json_schema_validators['jsd_349c888443b89a58_v1_3_0'] =\
    JSONSchemaValidator349C888443B89A58_v1_3_0()
json_schema_validators['jsd_3d923b184dc9a4ca_v1_3_0'] =\
    JSONSchemaValidator3D923B184Dc9A4Ca_v1_3_0()
json_schema_validators['jsd_4bb22af046fa8f08_v1_3_0'] =\
    JSONSchemaValidator4Bb22Af046Fa8F08_v1_3_0()
json_schema_validators['jsd_4eb56a614cc9a2d2_v1_3_0'] =\
    JSONSchemaValidator4Eb56A614Cc9A2D2_v1_3_0()
json_schema_validators['jsd_5b8639224cd88ea7_v1_3_0'] =\
    JSONSchemaValidator5B8639224Cd88Ea7_v1_3_0()
json_schema_validators['jsd_5db21b8e43fab7d8_v1_3_0'] =\
    JSONSchemaValidator5Db21B8E43FaB7D8_v1_3_0()
json_schema_validators['jsd_70ad397649e9b4d3_v1_3_0'] =\
    JSONSchemaValidator70Ad397649E9B4D3_v1_3_0()
json_schema_validators['jsd_82918a1b4d289c5c_v1_3_0'] =\
    JSONSchemaValidator82918A1B4D289C5C_v1_3_0()
json_schema_validators['jsd_84b37ae54c59ab28_v1_3_0'] =\
    JSONSchemaValidator84B37Ae54C59Ab28_v1_3_0()
json_schema_validators['jsd_81bb4804405a8d2f_v1_3_0'] =\
    JSONSchemaValidator81Bb4804405A8D2F_v1_3_0()
json_schema_validators['jsd_84ad8b0e42cab48a_v1_3_0'] =\
    JSONSchemaValidator84Ad8B0E42CaB48A_v1_3_0()
json_schema_validators['jsd_84b33a9e480abcaf_v1_3_0'] =\
    JSONSchemaValidator84B33A9E480ABcaf_v1_3_0()
json_schema_validators['jsd_819f9aa54feab7bf_v1_3_0'] =\
    JSONSchemaValidator819F9Aa54FeaB7Bf_v1_3_0()
json_schema_validators['jsd_8fa8eb404a4a8d96_v1_3_0'] =\
    JSONSchemaValidator8Fa8Eb404A4A8D96_v1_3_0()
json_schema_validators['jsd_ba9dc85b4b8a9a17_v1_3_0'] =\
    JSONSchemaValidatorBa9DC85B4B8A9A17_v1_3_0()
json_schema_validators['jsd_c9809b6744f8a502_v1_3_0'] =\
    JSONSchemaValidatorC9809B6744F8A502_v1_3_0()
json_schema_validators['jsd_b9855ad54ae98156_v1_3_0'] =\
    JSONSchemaValidatorB9855Ad54Ae98156_v1_3_0()
json_schema_validators['jsd_b7bcaa084e2b90d0_v1_3_0'] =\
    JSONSchemaValidatorB7BcAa084E2B90D0_v1_3_0()
json_schema_validators['jsd_cd98780f4888a66d_v1_3_0'] =\
    JSONSchemaValidatorCd98780F4888A66D_v1_3_0()
json_schema_validators['jsd_cd8469e647caab0e_v1_3_0'] =\
    JSONSchemaValidatorCd8469E647CaAb0E_v1_3_0()
json_schema_validators['jsd_d0a4b88145aabb51_v1_3_0'] =\
    JSONSchemaValidatorD0A4B88145AaBb51_v1_3_0()
json_schema_validators['jsd_888f585c49b88441_v1_3_0'] =\
    JSONSchemaValidator888F585C49B88441_v1_3_0()
json_schema_validators['jsd_d888ab6d4d59a8c1_v1_3_0'] =\
    JSONSchemaValidatorD888Ab6D4D59A8C1_v1_3_0()
json_schema_validators['jsd_f5947a4c439a8bf0_v1_3_0'] =\
    JSONSchemaValidatorF5947A4C439A8Bf0_v1_3_0()
json_schema_validators['jsd_8db939744649a782_v1_3_0'] =\
    JSONSchemaValidator8Db939744649A782_v1_3_0()
json_schema_validators['jsd_eb8249e34f69b0f1_v1_3_0'] =\
    JSONSchemaValidatorEb8249E34F69B0F1_v1_3_0()
json_schema_validators['jsd_f6826a8e41bba242_v1_3_0'] =\
    JSONSchemaValidatorF6826A8E41BbA242_v1_3_0()
json_schema_validators['jsd_aeb9eb67460b92df_v1_3_0'] =\
    JSONSchemaValidatorAeb9Eb67460B92Df_v1_3_0()
json_schema_validators['jsd_b888792d43baba46_v1_3_0'] =\
    JSONSchemaValidatorB888792D43BaBa46_v1_3_0()
json_schema_validators['jsd_c3b3c9ef4e6b8a09_v1_3_0'] =\
    JSONSchemaValidatorC3B3C9Ef4E6B8A09_v1_3_0()
json_schema_validators['jsd_89b2fb144f5bb09b_v1_3_0'] =\
    JSONSchemaValidator89B2Fb144F5BB09B_v1_3_0()
json_schema_validators['jsd_f49548c54be8a3e2_v1_3_0'] =\
    JSONSchemaValidatorF49548C54Be8A3E2_v1_3_0()
json_schema_validators['jsd_ffa748cc44e9a437_v1_3_0'] =\
    JSONSchemaValidatorFfa748Cc44E9A437_v1_3_0()
json_schema_validators['jsd_17a82ac94cf99ab0_v1_3_0'] =\
    JSONSchemaValidator17A82Ac94Cf99Ab0_v1_3_0()
json_schema_validators['jsd_33aab9b842388023_v1_3_0'] =\
    JSONSchemaValidator33AaB9B842388023_v1_3_0()
json_schema_validators['jsd_23896b124bd8b9bf_v1_3_0'] =\
    JSONSchemaValidator23896B124Bd8B9Bf_v1_3_0()
json_schema_validators['jsd_209509d247599e19_v1_3_0'] =\
    JSONSchemaValidator209509D247599E19_v1_3_0()
json_schema_validators['jsd_92acda91406aa050_v1_3_0'] =\
    JSONSchemaValidator92AcDa91406AA050_v1_3_0()
json_schema_validators['jsd_d9bdb9034df99dba_v1_3_0'] =\
    JSONSchemaValidatorD9BdB9034Df99Dba_v1_3_0()
json_schema_validators['jsd_eeb168eb41988e07_v1_3_0'] =\
    JSONSchemaValidatorEeb168Eb41988E07_v1_3_0()
json_schema_validators['jsd_eba669054e08a60e_v1_3_0'] =\
    JSONSchemaValidatorEba669054E08A60E_v1_3_0()
json_schema_validators['jsd_6284db4649aa8d31_v1_3_0'] =\
    JSONSchemaValidator6284Db4649Aa8D31_v1_3_0()
json_schema_validators['jsd_9ba14a9e441b8a60_v1_3_0'] =\
    JSONSchemaValidator9Ba14A9E441B8A60_v1_3_0()
json_schema_validators['jsd_b2b8cb91459aa58f_v1_3_0'] =\
    JSONSchemaValidatorB2B8Cb91459AA58F_v1_3_0()
json_schema_validators['jsd_b9b48ac8463a8aba_v1_3_0'] =\
    JSONSchemaValidatorB9B48Ac8463A8Aba_v1_3_0()
json_schema_validators['jsd_c2b5fb764d888375_v1_3_0'] =\
    JSONSchemaValidatorC2B5Fb764D888375_v1_3_0()
json_schema_validators['jsd_ca91da84401abba1_v1_3_0'] =\
    JSONSchemaValidatorCa91Da84401ABba1_v1_3_0()
json_schema_validators['jsd_149aa93b4ddb80dd_v1_3_0'] =\
    JSONSchemaValidator149AA93B4Ddb80Dd_v1_3_0()
json_schema_validators['jsd_e2adba7943bab3e9_v1_3_0'] =\
    JSONSchemaValidatorE2AdBa7943BaB3E9_v1_3_0()
json_schema_validators['jsd_0b836b7b4b6a9fd5_v1_3_0'] =\
    JSONSchemaValidator0B836B7B4B6A9Fd5_v1_3_0()
json_schema_validators['jsd_0a9c988445cb91c8_v1_3_0'] =\
    JSONSchemaValidator0A9C988445Cb91C8_v1_3_0()
json_schema_validators['jsd_09b0f9ce4239ae10_v1_3_0'] =\
    JSONSchemaValidator09B0F9Ce4239Ae10_v1_3_0()
json_schema_validators['jsd_2499e9ad42e8ae5b_v1_3_0'] =\
    JSONSchemaValidator2499E9Ad42E8Ae5B_v1_3_0()
json_schema_validators['jsd_1e962af345b8b59f_v1_3_0'] =\
    JSONSchemaValidator1E962Af345B8B59F_v1_3_0()
json_schema_validators['jsd_21a6db2540298f55_v1_3_0'] =\
    JSONSchemaValidator21A6Db2540298F55_v1_3_0()
json_schema_validators['jsd_3086c9624f498b85_v1_3_0'] =\
    JSONSchemaValidator3086C9624F498B85_v1_3_0()
json_schema_validators['jsd_3cb24acb486b89d2_v1_3_0'] =\
    JSONSchemaValidator3Cb24Acb486B89D2_v1_3_0()
json_schema_validators['jsd_5889fb844939a13b_v1_3_0'] =\
    JSONSchemaValidator5889Fb844939A13B_v1_3_0()
json_schema_validators['jsd_6f9819e84178870c_v1_3_0'] =\
    JSONSchemaValidator6F9819E84178870C_v1_3_0()
json_schema_validators['jsd_7989f86846faaf99_v1_3_0'] =\
    JSONSchemaValidator7989F86846FaAf99_v1_3_0()
json_schema_validators['jsd_70a479a6462a9496_v1_3_0'] =\
    JSONSchemaValidator70A479A6462A9496_v1_3_0()
json_schema_validators['jsd_7e92f9eb46db8320_v1_3_0'] =\
    JSONSchemaValidator7E92F9Eb46Db8320_v1_3_0()
json_schema_validators['jsd_8da0391947088a5a_v1_3_0'] =\
    JSONSchemaValidator8Da0391947088A5A_v1_3_0()
json_schema_validators['jsd_848b5a7b4f9b8c12_v1_3_0'] =\
    JSONSchemaValidator848B5A7B4F9B8C12_v1_3_0()
json_schema_validators['jsd_a4b6c87a4ffb9efa_v1_3_0'] =\
    JSONSchemaValidatorA4B6C87A4Ffb9Efa_v1_3_0()
json_schema_validators['jsd_9e857b5a4a0bbcdb_v1_3_0'] =\
    JSONSchemaValidator9E857B5A4A0BBcdb_v1_3_0()
json_schema_validators['jsd_af8d7b0e470b8ae2_v1_3_0'] =\
    JSONSchemaValidatorAf8D7B0E470B8Ae2_v1_3_0()
json_schema_validators['jsd_cdab9b474899ae06_v1_3_0'] =\
    JSONSchemaValidatorCdab9B474899Ae06_v1_3_0()
json_schema_validators['jsd_aeb4dad04a99bbe3_v1_3_0'] =\
    JSONSchemaValidatorAeb4Dad04A99Bbe3_v1_3_0()
json_schema_validators['jsd_bab6c9e5440885cc_v1_3_0'] =\
    JSONSchemaValidatorBab6C9E5440885Cc_v1_3_0()
json_schema_validators['jsd_d9a1fa9c4068b23c_v1_3_0'] =\
    JSONSchemaValidatorD9A1Fa9C4068B23C_v1_3_0()
json_schema_validators['jsd_80acb88e4ac9ac6d_v1_3_0'] =\
    JSONSchemaValidator80AcB88E4Ac9Ac6D_v1_3_0()
json_schema_validators['jsd_f09319674049a7d4_v1_3_0'] =\
    JSONSchemaValidatorF09319674049A7D4_v1_3_0()
json_schema_validators['jsd_e6b3db8046c99654_v1_3_0'] =\
    JSONSchemaValidatorE6B3Db8046C99654_v1_3_0()
json_schema_validators['jsd_cf9418234d9ab37e_v1_3_0'] =\
    JSONSchemaValidatorCf9418234D9AB37E_v1_3_0()
json_schema_validators['jsd_f3b26b5544cabab9_v1_3_0'] =\
    JSONSchemaValidatorF3B26B5544CaBab9_v1_3_0()
json_schema_validators['jsd_d8a619974a8a8c48_v1_3_0'] =\
    JSONSchemaValidatorD8A619974A8A8C48_v1_3_0()
json_schema_validators['jsd_0c8f7a0b49b9aedd_v1_3_0'] =\
    JSONSchemaValidator0C8F7A0B49B9Aedd_v1_3_0()
json_schema_validators['jsd_8cb6783b4faba1f4_v1_3_0'] =\
    JSONSchemaValidator8Cb6783B4FabA1F4_v1_3_0()
json_schema_validators['jsd_4dbe3bc743a891bc_v1_3_0'] =\
    JSONSchemaValidator4Dbe3Bc743A891Bc_v1_3_0()
json_schema_validators['jsd_fb9beb664f2aba4c_v1_3_0'] =\
    JSONSchemaValidatorFb9BEb664F2ABa4C_v1_3_0()
json_schema_validators['jsd_bc8aab4746ca883d_v1_3_0'] =\
    JSONSchemaValidatorBc8AAb4746Ca883D_v1_3_0()
json_schema_validators['jsd_7fbe4b804879baa4_v1_3_0'] =\
    JSONSchemaValidator7Fbe4B804879Baa4_v1_3_0()
json_schema_validators['jsd_828828f44f28bd0d_v1_3_0'] =\
    JSONSchemaValidator828828F44F28Bd0D_v1_3_0()
json_schema_validators['jsd_2f97e8fa45f8b2a3_v1_3_0'] =\
    JSONSchemaValidator2F97E8Fa45F8B2A3_v1_3_0()
json_schema_validators['jsd_ac8ae94c4e69a09d_v1_3_0'] =\
    JSONSchemaValidatorAc8AE94C4E69A09D_v1_3_0()


def json_schema_validate(model):
    """Factory function for creating JSONSchemaValidator objects.

    Args:
        model(basestring).

    Returns:
        JSONSchemaValidator: The created JSONSchemaValidator object.

    Raises:
        MalformedRequest.
    """
    return json_schema_validators.get(model, JSONSchemaValidator())
