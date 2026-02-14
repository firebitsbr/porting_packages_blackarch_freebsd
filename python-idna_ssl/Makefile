PORTNAME=	python-idna_ssl
DISTVERSION=	1.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Patch ssl.match_hostname for Unicode(idna) domains support.
WWW=		https://github.com/aio-libs/idna-ssl

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/flake8 \
		??/py-idna@${PY_FLAVOR} \
		??/py-isort@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
