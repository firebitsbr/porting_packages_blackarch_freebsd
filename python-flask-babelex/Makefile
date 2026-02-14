PORTNAME=	python-flask-babelex
DISTVERSION=	0.9.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	i18n and l10n support for Flask based on Babel and pytz.
WWW=		https://github.com/mrjoes/flask-babelex

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-babel@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-speaklater@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
