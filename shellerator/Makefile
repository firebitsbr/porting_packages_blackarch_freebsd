PORTNAME=	shellerator
DISTVERSION=	57.e0f3b38
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple command-line tool aimed to help pentesters quickly generate one-liner reverse/bind shells in multiple languages.
WWW=		https://github.com/ShutdownRepo/shellerator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-console-menu@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-simple-term-menu@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
