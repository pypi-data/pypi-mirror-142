# -*- coding: utf-8 -*-

import riskscore.creditscore as creditscore


try:
    import riskscore.mechinelearning as mechinelearning
except ImportError:
    print('riskscore包creditscore模块导入成功，但是mechinelearning模块导入失败。mechinelearning模块中，以下库是必须的，\
          你可能缺少了其中的一个或者多个：xlsxwriter、joblib、xgboost、openpyxl。如你不使用mechinelearning模块则无需理会本提示。')

__all__=['creditscore','mechinelearning']
