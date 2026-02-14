PORTNAME=	gtfoblookup
DISTVERSION=	69.cc50e6e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Offline command line lookup utility for GTFOBins and LOLBAS.
WWW=		https://github.com/nccgroup/GTFOBLookup

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-appdirs@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
