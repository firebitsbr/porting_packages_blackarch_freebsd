PORTNAME=	pcode2code
DISTVERSION=	6.65ae983
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	VBA p-code decompiler.
WWW=		https://github.com/Big5-sec/pcode2code

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		devel/git

RUN_DEPENDS=	??/py-pcodedmp@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
