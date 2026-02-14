PORTNAME=	certsync
DISTVERSION=	0.1.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Dump NTDS remotely without DRSUAPI: using golden certificate and UnPAC the hash.
WWW=		https://github.com/zblurx/certsync

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/certipy \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
