import numpy as np

rename_dict = {
    "about_whole_nation_recoded": {
        "rus": "Говорит ли автор об этносе в целом?",
        "level": "ethnicity",
        "measument_level": "nominal",
        "recode": {
            "1": {
                "value": 1,
                "label": "yes"
            },
            "0": {
                "value": 0,
                "label": "no"
            },
            "unk": {
                "value": np.nan,
                "label": "unk"
            }
        }
    },
    "assessor": "Кодировщик",
    "comment": "Комментарий кодировщика",
    "date": "Дата кодирования",
    "document.id": "ID документа",
    "do_text_make_sense_raw": {
        "rus": "Понятно ли Вам о чём текст?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            "yes": {
                "value": 1,
                "label": "yes"
            },
            "no": {
                "value": 0,
                "label": "no"
            },
            "lang": {
                "value": 0,
                "label": "no"
            },
            "joke": {
                "value": 0,
                "label": "no"
            },
        }
    },
    "encourage_aggression_meaning": {
        "rus": "Призывает ли автор к насильственному оффлайновому действию по отношению к этническому персонажу?",
        "level": "ethnicity",
        "measument_level": "ordinal",
        "recode": {
            "yes latent": {
                "value": 1,
                "label": "yes latent"
            },
            "no": {
                "value": 0,
                "label": "no"
            },
            "yes open": {
                "value": 2,
                "label": "yes open"
            }
        }
    },
    "eth_group_to_code": "Этническая группа, по которой производилось кодирование", # особый случай
    "has_eth_conflict_raw": {
        "rus": "Прослеживается ли конфликт между этническими группами?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            "unk": {
                "value": np.nan,
                "label": "unk"
            },
            "no": {
                "value": 0,
                "label": "no"
            },
            "yes": {
                "value": 1,
                "label": "yes"
            }
        }
    },
    "has_ethnonym_raw": {
        "rus": "Содержит ли текст этноним или название этнической группы?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            "unk": {
                "value": np.nan,
                "label": "unk"
            },
            "no": {
                "value": 0,
                "label": "no"
            },
            "one": {
                "value": 1,
                "label": "one"
            },
            "several": {
                "value": 2,
                "label": "several"
            },
        }
    },
    "has_pos_eth_interaction_raw": {
        "rus": "Прослеживается ли позитивное взаимодействие между этническими группами?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            "unk": {
                "value": np.nan,
                "label": "unk"
            },
            "no": {
                "value": 0,
                "label": "no"
            },
            "yes": {
                "value": 1,
                "label": "yes"
            }
        }
    },
    "has_topic_culture": {
        "rus": "Имеется ли тема культуры?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_daily_routine": {
        "rus": "Имеется ли повседневная тематика?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_economics": {
        "rus": "Имеется ли тема экономики?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_ethicity": {
        "rus": "Имеется ли тема этничности?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_history": {
        "rus": "Имеется ли тема истории?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_humour": {
        "rus": "Имеется ли тема юмора?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_migration": {
        "rus": "Имеется ли тема миграции?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_other": {
        "rus": "Имеется ли какая-то другая тема?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_politics": {
        "rus": "Имеется ли тема политики?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_religion": {
        "rus": "Имеется ли тема религии?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "has_topic_society_social": {
        "rus": "Имеется ли социальная тема?",
        "level": "answer",
        "measument_level": "nominal",
        "recode": {
            1.0: {
                "value": 1,
                "label": "yes"
            },
            0.0: {
                "value": 0,
                "label": "no"
            }
        }
    },
    "is_ethicity_aggressor_meaning": {
        "rus": "Этнический персонаж (группа) оценивается как жертва или как агрессор?",
        "level": "ethnicity",
        "measument_level": "nominal",
        "recode": {
            "irrel": {
                "value": np.nan,
                "label": "irrelevant"
            },
            "agressor": {
                "value": 1,
                "label": "agressor"
            },
            "victim": {
                "value": 0,
                "label": "victim"
            }
        }
    },
    "is_ethicity_dangerous_meaning": {
        "rus": "Этнический персонаж (группа) оценивается как опасный?",
        "level": "ethnicity",
        "measument_level": "nominal",
        "recode": {
            "no": {
                "value": 0,
                "label": "no"
            },
            "yes": {
                "value": 1,
                "label": "yes"
            },
            "irrel": {
                "value": np.nan,
                "label": "irrel"
            }
        }
    },
    "is_ethicity_superior_meaning": {
        "rus": "Этнический персонаж (группа) оценивается как высший или низший?",
        "level": "ethnicity",
        "measument_level": "nominal",
        "recode": {
            "no": {
                "value": 0,
                "label": "no"
            },
            "high": {
                "value": 2,
                "label": "high"
            },
            "low": {
                "value": 1,
                "label": "low"
            },
            "irrel": {
                "value": np.nan,
                "label": "irrel"
            }
        }
    },
    "is_text_neg_raw": {
        "rus": "Есть ли текст негативный сентимент?",
        "level": "answer",
        "measument_level": "ordinal",
        "recode": {
            "no": {
                "value": 0,
                "label": "no"
            },
            "weak": {
                "value": 1,
                "label": "weak"
            },
            "strong": {
                "value": 2,
                "label": "strong"
            },
            "unk": {
                "value": np.nan,
                "label": "unk"
            }
        }
    },
    "is_text_positive_raw": {
        "rus": "Есть ли текст позитивный сентимент?",
        "level": "answer",
        "measument_level": "ordinal",
        "recode": {
            "no": {
                "value": 0,
                "label": "no"
            },
            "weak": {
                "value": 1,
                "label": "weak"
            },
            "strong": {
                "value": 2,
                "label": "strong"
            },
            "unk": {
                "value": np.nan,
                "label": "unk"
            }
        }
    },
    "opinion_about_ethnonym_recoded": {
        "rus": "Каково авторское отношение к этническому персонажу?",
        "level": "ethnicity",
        "measument_level": "ordinal",
        "recode": {
            1.0: {
                "value": 2,
                "label": "positive"
            },
            -1.0: {
                "value": 0,
                "label": "negative"
            },
            0.0: {
                "value": 1,
                "label": "neutral"
            }
        }
    },
    "represent_ethicity_meaning": {
        "rus": "Принадлежит ли автор к этнической группе?",
        "level": "ethnicity",
        "measument_level": "nominal",
        "recode": {
            "no": {
                "value": 0,
                "label": "no"
            },
            "yes": {
                "value": 1,
                "label": "yes"
            },
            "unk": {
                "value": np.nan,
                "label": "unk"
            }
        }
    },
    "seed_eth_group": "Этноним, с которого начиналось оценивание",
    "source": "VK или IQBuzz",
    "stage": "Стадия кодирования",
}