PORTNAME=	python2-flask-mail
DISTVERSION=	0.9.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Flask extension for sending email.
WWW=		https://pypi.org/project/Flask-Mail/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blinker@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
