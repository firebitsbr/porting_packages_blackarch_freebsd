PORTNAME=	python-frida
DISTVERSION=	17.6.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers.
WWW=		https://pypi.org/project/frida/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR} \
		www/node \
		www/npm

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-tomlkit@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
