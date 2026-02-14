PORTNAME=	python-telethon
DISTVERSION=	1.25.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Full-featured Telegram client library for Python 3.
WWW=		https://pypi.org/project/telethon/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pyaes@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
