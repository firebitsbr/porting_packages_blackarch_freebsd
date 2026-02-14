PORTNAME=	python-notify_py
DISTVERSION=	0.3.43
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python Module for sending cross-platform desktop notifications.
WWW=		https://github.com/ms7m/notify-py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/# \
		??/https://github.com/ms7m/notify-py/blob/master/pyproject.toml \
		??/libnotify \
		??/py-jeepney@${PY_FLAVOR} \
		??/py-loguru@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
