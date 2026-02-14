PORTNAME=	uberfile
DISTVERSION=	14.4414c2a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CLI tool for the generation of downloader oneliners for UNIX-like or Windows systems.
WWW=		https://github.com/ShutdownRepo/uberfile

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
