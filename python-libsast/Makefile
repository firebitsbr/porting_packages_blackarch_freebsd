PORTNAME=	python-libsast
DISTVERSION=	3.1.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A generic SAST core built on top of semgrep and regex.
WWW=		https://pypi.org/project/libsast/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pyaml@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/semgrep \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
