import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'dbg': {
            'format': '%(levelname)s  %(asctime)s %(message)s'
        },
        'wrn': {
            'format': '%(levelname)s  %(asctime)s %(pathname)s %(message)s'
        },
        'err': {
            'format': '%(levelname)s  %(asctime)s %(pathname)s %(exc_info)s %(message)s'
        },
        'glf': {
            'format': '%(levelname)s  %(module)s %(message)s'
        },
        'elf': {
            'format': '%(asctime)s %(levelname)s %(message)s  %(pathname)s %(exc_info)s'
               },
        'slf': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'mail': {
            'format': '%(asctime)s %(levelname)s %(message)s  %(pathname)s '
               }

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
####CONSOLE###############################
        'consoled': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'dbg'
        },
       'consolew': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'wrn'
        },
        'consolee': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'err'
        },
###########################################################################
        'generalfilelog': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            "filename": "general.log",
            'formatter': 'glf'
        },
        'errorsfilelog': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            "filename": "errors.log",
            'formatter': 'elf'
        },
        'secfilelog': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            "filename": "security.log",
            'formatter': 'slf'
        },
############################################################################
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['consoled','consolew','consolee','mail_admins'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errorsfilelog'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errorsfilelog'],
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errorsfilelog'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errorsfilelog'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['secfilelog'],
            'propagate': False,
        }
    }
}
