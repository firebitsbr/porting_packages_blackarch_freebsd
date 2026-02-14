PORTNAME=	python2-flask-babel
DISTVERSION=	0.12.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Adds i18n/l10n support to Flask applications
WWW=		https://pypi.org/project/Flask-Babel/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-babel@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-speaklater@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
